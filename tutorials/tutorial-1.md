# INFO0948 - Tutorial 1 : Introduction to RoS

Welcome to the INFO0948 course! This tutorial will guide you through key milestones to help you grasp the fundamentals. Each milestone includes an estimated time commitment, links to the relevant documentation, and a brief description of the content covered.

An assignment is provided at the end of the tutorial to assess and apply what you learnt during the tutorial. 

**Note**: In the links provided, you should always skip the `Prerequisites` part as it is not necessary
## 1. Get started with Concepts & CLI Tools
This first part of the tutorial will make you understand the core principles of RoS so that you have an overview about how everything is working altogether. You will mainly use the terminal to run commands and interact with GUI.
### Understanding the principles of RoS nodes
- **Time Needed:** ~10 minutes
- **Start Here:** [Understanding nodes](https://docs.ros.org/en/foxy/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes.html)
- **Note:** -

### Understanding the principles of RoS topics
- **Time Needed:** ~20 minutes
- **Start Here:** [Understanding topics](https://docs.ros.org/en/foxy/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Topics/Understanding-ROS2-Topics.html)
- **Note:** -

### Understanding the principles of RoS services
- **Time Needed:** ~10 minutes
- **Start Here:** [Understanding services](https://docs.ros.org/en/foxy/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Services/Understanding-ROS2-Services.html)
- **Note:** -

### Understanding the principles of RoS actions
- **Time Needed:** ~15 minutes
- **Start Here:** [Understanding actions](link_to_advanced_techniques)
- **Note:** -

### Become familiar with the logging tool `rqt_console`
- **Time Needed:** ~5 minutes
- **Start Here:** [Using `rqt_console` to view logs](link_to_troubleshooting)
- **Note:** -

## 2. Time to make your own Packages !
### Colcon: the tool to build you packages and workspaces
- **Time Needed:** ~20 minutes
- **Start Here:** [Using `colcon` to build packages](https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Colcon-Tutorial.html)
- **Note:** -

### Creating your own workspace for a project
- **Time Needed:** ~20 minutes
- **Start Here:** [Creating a workspace](https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html)
- **Note:** -

### Cerating your own packages inside a workspace
- **Time Needed:** ~15 minutes
- **Start Here:** [Creating a package](https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Creating-Your-First-ROS2-Package.html)
- **Note:** -.

### Writing a publisher and subscriber node in Python
- **Time Needed:** ~20 minutes
- **Start Here:** [Writing a simple publisher and subscriber (Python)](https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html)
- **Note:** -

## Hands-on : An Hyperbolic Node 
Apply what you've learned in the tutorial to a simple assignement. 

You will download ... to have all the necessary files.
Your **goal** is to write a node inside ... that is named ... and will listen to messages published to the topic ... .
The message type is simply ... .
Then, it should apply the `tanh` function to each value received.
The result must be then published to the topic ... .
To verify that your code is working, you may launch the entire stuff with:
``.