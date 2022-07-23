# FaceMaskDoorLockDetectionSystem

This project is a whole system, its made using 3 languages and all work together.
The system consists of 4 parts, IOS application(receiving pictures as well as overiding the lock), Python Program(to detect the mask), A Node Mcu with a servo connected to it acting as the door lock(A rely would be inplace of the servo), and A data base(google Firebase)
The python program is conntected to a camera feed, The python program analysis the feed and using machine learning detects if there is a face in the feed, if a face is detected
the program detects if the person in the camera feed is wearing a mask or not, accordingly the program sends a signle to the NodeMCU, if the person is wearing a mask the
program sends an signal wirelessly to the NodeMCU to unlock the door, If the program detects that the person is not wearing a mask, 
The program sends a singal to the NodeMCU to lock the door as well as The program will take a picture of the
person that is not wearing the masek and send it to the data base on the cloud, The IOS Application automatically detects that there has been a new picture uploaded to the databse
and downloads the picture and displays it on the Phone wich will give a notificaion that there is a person that is not wearing a mask.


<img src="https://github.com/404dn/FaceMaskDoorLockDetectionSystem/blob/master/pictuers/2.PNG" width="350" height="250">


<img src="https://github.com/404dn/FaceMaskDoorLockDetectionSystem/blob/master/pictuers/3.PNG" width="500" height="550">


<img src="https://github.com/404dn/FaceMaskDoorLockDetectionSystem/blob/master/pictuers/5.PNG" width="500" height="550">


<img src="https://github.com/404dn/FaceMaskDoorLockDetectionSystem/blob/master/pictuers/node%20mcupng.png" width="500" height="550">
