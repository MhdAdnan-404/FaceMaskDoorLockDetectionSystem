# import the necessary packages
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from imutils.video import VideoStream
import numpy as np
import imutils
import cv2
import requests
import pyrebase
import win32gui
from PIL import ImageGrab
import threading

counter = 0
signal_sent = True
previous_lbl = ""

config = {
   
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
db = firebase.database()


def sc_Window():
    global counter
    path_onlocal = 'sc/result' + str(counter) + '.png'
    hwnd = win32gui.FindWindow(None, r'Frame')
    dimensions = win32gui.GetWindowRect(hwnd)
    im = ImageGrab.grab(dimensions)
    im.save(path_onlocal)
    print("screen shot taken")
    send_img_firebase()
    counter += 1


def send_img_firebase():
    # storage
    path_on_cloud = 'images/Sc' + str(counter) + '.png'
    path_local = 'sc/result' + str(counter) + '.png'
    storage.child(path_on_cloud).put(path_local)  # make async
    download_url = storage.child(path_on_cloud).get_url(path_on_cloud)
    print(download_url)
    # RealTime DataBase
    data = {'Img_name': download_url}
    db.set(data)


timer = threading.Timer(3.0, sc_Window)


def on_detect():
    global timer
    timer = threading.Timer(2.0, sc_Window)
    timer.start()
    print("timer started ")


def detect_and_predict_mask(frame, faceNet, maskNet):
    # grab the dimensions of the frame and then construct a blob
    # from it
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 1.0, (224, 224), (104.0, 177.0, 123.0))

    # pass the blob through the network and obtain the face detections
    faceNet.setInput(blob)
    detections = faceNet.forward()
    print(detections.shape)

    # initialize our list of faces, their corresponding locations,
    # and the list of predictions from our face mask network
    faces = []
    locs = []
    preds = []

    # loop over the detections
    for i in range(0, detections.shape[2]):
        # extract the confidence (i.e., probability) associated with
        # the detection
        confidence = detections[0, 0, i, 2]

        # filter out weak detections by ensuring the confidence is
        # greater than the minimum confidence
        if confidence > 0.5:
            # compute the (x, y)-coordinates of the bounding box for
            # the object
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            # ensure the bounding boxes fall within the dimensions of
            # the frame
            (startX, startY) = (max(0, startX), max(0, startY))
            (endX, endY) = (min(w - 1, endX), min(h - 1, endY))

            # extract the face ROI, convert it from BGR to RGB channel
            # ordering, resize it to 224x224, and preprocess it
            face = frame[startY:endY, startX:endX]
            face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
            face = cv2.resize(face, (224, 224))
            face = img_to_array(face)
            face = preprocess_input(face)

            # add the face and bounding boxes to their respective
            # lists
            faces.append(face)
            locs.append((startX, startY, endX, endY))

    if len(faces) != 1:
        # more than two seconds
        global signal_sent
        signal_sent = False
    if len(faces) == 0:
        timer.cancel()

    # only make a predictions if at least one face was detected
    if len(faces) > 0:
        # for faster inference we'll make batch predictions on *all*
        # faces at the same time rather than one-by-one predictions
        # in the above `for` loop
        faces = np.array(faces, dtype="float32")
        preds = maskNet.predict(faces, batch_size=32)

    # return a 2-tuple of the face locations and their corresponding
    # locations
    return (locs, preds)


# load our serialized face detector model from disk
prototxtPath = r"face_detector\deploy.prototxt"
weightsPath = r"face_detector\res10_300x300_ssd_iter_140000.caffemodel"
faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)

# load the face mask detector model from disk
maskNet = load_model("mask_detector.model")

# initialize the video stream
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()

# loop over the frames from the video stream
while True:
    # grab the frame from the threaded video stream and resize it
    # to have a maximum width of 400 pixels
    frame = vs.read()
    frame = imutils.resize(frame, width=400)

    # detect faces in the frame and determine if they are wearing a
    # face mask or not
    (locs, preds) = detect_and_predict_mask(frame, faceNet, maskNet)

    # loop over the detected face locations and their corresponding
    # locations
    for (box, pred) in zip(locs, preds):
        # unpack the bounding box and predictions
        (startX, startY, endX, endY) = box
        (mask, withoutMask) = pred

        # determine the class label and color we'll use to draw
        # the bounding box and text
        label = "Mask" if mask > withoutMask else "No Mask"
        color = (0, 255, 0) if label == "Mask" else (0, 0, 255)

        # send signal to the servo only if the mask label chnaged
        # send signal to firebase only if the face went off the screen and came back on

        if signal_sent == False:
            if label == "No Mask":
                # if more than two seconds
                # sc_Window()
                on_detect()
                # RealTimeDataBase
                print("Notifcation trigger")
                signal_sent = True

        if label != previous_lbl:
            if label == "Mask":
                r = requests.post('http://192.168.1.144/LED=ON')
                timer.cancel()
            elif label == "No Mask":
                r = requests.post('http://192.168.1.144/LED=OFF')
                on_detect()
        previous_lbl = label

        # include the probability in the label
        label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)

        # display the label and bounding box rectangle on the output
        # frame
        cv2.putText(frame, label, (startX, startY - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
        cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)

    # show the output frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
