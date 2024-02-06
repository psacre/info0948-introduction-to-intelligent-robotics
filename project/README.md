# Project
#### Introduction 
In this course, you will work with the third version of the turtle robot, namely TurtleBot3 Burger. The lab counts ten burger model robots (see Figure 1) to which you will have access during the semester. The TurtleBots can be controlled using the Robot Operating System 2 (ROS2). It is a set of open-source software libraries and tools that help you build robot applications. In addition to the state-of-the-art algorithms ROS2 already provides, you will have to code your own algorithms in Python. Each robot comes with a computer on which all the software you need is installed. Nevertheless, you will probably want to test your code with ROS2 and the simulation environment Gazebo on your own computer as the robots and their computer won't leave the lab. For this, please refer to the **setup** folder of this repository. 

<p align="center">
  <img src="./images/robot.png" width="200" />
</p>

The TurtleBots are equipped with a front camera and a LiDAR sensor that gives a 360°-scan of the surrounding environment in a range-and-bearing fashion. In the project of this course, you will use a single robot in a closed environment, where the only obstacles are inert walls. Testing and debugging your code in a real-world setup is a tedious work. For this reason, you will first develop your codes in simulation using Gazebo. We will provide you with the simulating environment. Examples of real-world and simulation environments are shown in Figure 2.


