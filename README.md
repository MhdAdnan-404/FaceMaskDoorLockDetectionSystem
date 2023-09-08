## Project


<br />

<div align="center">
  <h2 align="center">FaceMaskDoorLockDetectionSystem</h2>

  <p align="center">
    This system integrates an iOS application, Python program with machine learning-based mask detection, NodeMCU-controlled door lock, and a cloud database to enforce mask-wearing policies by automatically locking the door and notifying users with images of non-compliant individuals. 
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
    </li>
    <li><a href="#features">Features</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>
        
## About The Project



<h4>
  <p>
     the face mask detection system utilizes IoT devices equipped with cameras and sensors to monitor and enforce mask-wearing policies in various industries, providing real-time data and alerts through a cloud-based server to ensure compliance.
</h4>


<p align="right">(<a href="#Project">back to top</a>)</p>


## Built With

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=swift,cpp,py" />
  </a>
</p>

<h2 align="left"> The Software </h2>
<p><Strong>The server side</Strong>, I had the option of using python as I already Knew the language and had built similar tcp servers with it, but because there might be alot of messages that are going to be sent to the server in a short duration, I wanted a fast languge to avoid data loss, so i choose type script, and saw this as a good opportunity to learn the langauge.</p>

<p><Strong>The front end</Strong>, Previously i had used SWFIT which is IOS native langauge, but i wanted to learn something new, so i settled for Reacte Native, the advanatge of using Reacte native is the that its widely supported and there is alot of libraries that make it very easy to develop and application quickly, as well as it uses HTML for the UI elements and CSS for styling the elements which makes it infinitely easier, more over Reacte native when complied gives two files, one is for IOS and the other is for ANDRIOD so it saves alot of time if developing for both platforms.</p>

<h2 align="left"> The Hardware </h2>


<p align="center">
<img src="https://github.com/404dn/Driver_Behavior_Monitoring./blob/main/Photos/Screenshot%202023-07-03%20033036.png" alt="drawing" width="200"/>
</p>

<p>The system relies on TelTonika Device, FMC 130, This device is specifically made for this task, its built for monitoring all kinds of data and input from the vehicle, the device allows the user to preset some thersholds and parameters that determines when dose the device alert and under what conditions, as well as it sends location and speed based on a preset interval, the deivce can be connected to the nemours systems that are in the car and can display all sorts of data, the device comes with its own software for ease of programmability and deployment.</p>



<p align="right">(<a href="#Project">back to top</a>)</p>


## Features
<h3 align="left"> Speed </h3>
  <p align="center">
    <img src="https://github.com/404dn/Driver_Behavior_Monitoring./blob/main/Photos/2.png" alt="drawing" width="250"/>
    <img src="https://github.com/404dn/Driver_Behavior_Monitoring./blob/main/Photos/Screenshot%202023-07-03%20032324.png" alt="drawing" width="270"/>
  <p>
 
</div>
  <p>Determined by the intervals that are <Strong>preset</Strong> on the Teltonika device, a Message is sent to the application containing the speed and the locaion of the car at the pre-determined interval</p>

  <p>The graph shows the speed of the car over the time of the trip, as well as when <Strong>hovring</Strong> over any point, it will show the time and the speed at that point in the graph </p>

  <p>Additionally when clicking on the points on the map, it will show the time at which that speed was recorded</p>

-----------

  <h3 align="left"> Speeding</h3>
  <p align="center">
    <img src="https://github.com/404dn/Driver_Behavior_Monitoring./blob/main/Photos/3.png" alt="drawing" width="250"/>
    <img src="https://github.com/404dn/Driver_Behavior_Monitoring./blob/main/Photos/8.png" alt="drawing" width="250"/>
  <p>

</div>
  <p>Another feature is Detecting Speeding, Determined by the preset Parameters on the Device, if the car exceeds the speed that is set, This will trigger a message to be send to the application through the server, the message will incluce the speed and the location of the car at that time </p>

  <p> The graph shows all of the times the determined speed was broken in the form of a graph, hovering over the graph will show that value of that point as well as the time at which that speed was recored</p>

  <p>Additionally when clicking on the points on the map, it will show the time at which that speed was recorded</p>

-----------

  <h3 align="left"> Aggressive Acceleration</h3>
  <p align="center">
    <img src="https://github.com/404dn/Driver_Behavior_Monitoring./blob/main/Photos/234.png" alt="drawing" width="265"/>
    <img src="https://github.com/404dn/Driver_Behavior_Monitoring./blob/main/Photos/7658.png" alt="drawing" width="265"/>
  <p>
  



</div>
  <p>One of the main featuers that has a significant impact on the score of the driver is Aggressive Acceleration, The device allows two types of ways to measure Aggressive Acceleration, Either through G-Force, or through the speed Acceleration of the car </p>

  <p> The method that was chosen was the G-Force Acceleration, Like the speeding, The app shows all of the instances that the preset thershold was broken, and it showes it in a graph, and the user can hover over and drag over the graph and this shows the value of the Acceleration as well as the time, Additionally the instance as also shown on the map  </p>

  <p>Additionally when clicking on the points on the map, it will show the time at which that threshold was broken</p>


  <p align="right">(<a href="#Project">back to top</a>)</p>

  -----------


  <h3 align="left"> Aggressive Braking</h3>
  <p align="center">
    <img src="https://github.com/404dn/Driver_Behavior_Monitoring./blob/main/Photos/564.png" alt="drawing" width="265"/>
    <img src="https://github.com/404dn/Driver_Behavior_Monitoring./blob/main/Photos/4.png" alt="drawing" width="265"/>
  <p>

</div>
  <p>Another Measure Featuer of the system is detecting any aggresive braking, A threshold that is preset on device as well as the accelerometer, a trigger will be sent to the server when the threshold is broken, Similarly all of the instances are displayed in graph form as well as on the map</p>

  <p> The graph shows all of the times when a trigger was sent to the server from the device, hovering over the graph shows the specific value as well as the time at which that value was recored  </p>

  <p>Additionally when clicking on the points on the map, it will show the time at which that value was recorded</p>


  <p align="right">(<a href="#Project">back to top</a>)</p>



## License

See `LICENSE.md` for more information.

<p align="right">(<a href="#Project">back to top</a>)</p>



