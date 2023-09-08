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
<p>The software side of the system encompasses an iOS application for user interaction to override the lock, a Python program with machine learning capabilities for real-time mask detection in camera feeds, and cloud-based data management to facilitate automatic alerts to the ios application as well as storing the pictures .</p>
<p align="center">

<img src="https://github.com/404dn/FaceMaskDoorLockDetectionSystem/blob/master/Pictuers/5.PNG" alt="drawing" width="200"/>
<img src="https://github.com/404dn/FaceMaskDoorLockDetectionSystem/blob/master/Pictuers/3.PNG" alt="drawing" width="200"/>  
<img src="https://github.com/404dn/FaceMaskDoorLockDetectionSystem/blob/master/Pictuers/2.PNG" alt="drawing" width="200"/>  
</p>



<h2 align="left"> The Hardware </h2>
<p>
  On the hardware side, the system utilizes a NodeMCU microcontroller with a servo (or relay) to physically control the door lock, serving as the interface between the software and the door; this hardware component receives signals from the Python program for door locking and unlocking based on mask detection, contributing to the system's access control functionality.
</p>

<p align="center">
<img src="https://github.com/404dn/FaceMaskDoorLockDetectionSystem/blob/master/Pictuers/node%20mcupng.png" alt="drawing" width="500"/>
</p>

<p>The system uses a NodeMCU that communicates with the python programe through the web and locks and unlocks the door.</p>



<p align="right">(<a href="#Project">back to top</a>)</p>


## License

See `LICENSE.md` for more information.

<p align="right">(<a href="#Project">back to top</a>)</p>



