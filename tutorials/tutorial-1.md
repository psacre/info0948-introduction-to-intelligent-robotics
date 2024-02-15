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

## 3. Homework: A Rotating Node
The goal of this homework is to apply the concepts you learned during the first tutorial. You have to create a ROS2 package that contains a node that retrieves a vector from a topic, rotates it around a given axis, and publishes the result on another topic. To do so, follow the procedure below:
  1. Create a workspace called <tt>tutorials_ws</tt>.
  2. Within this workspace, create a package called <tt>tuto_1</tt>.
  3. Create a python file <tt>rotation_node.py</tt> in the appropriate folder of your package <tt>tuto_1</tt>.
  4. Modify the files <tt>setup.py</tt> and <tt>package.xml</tt> so that the node you will write in <tt>rotation_node.py</tt> can be run with the command <tt>ros2 run tuto_1 rotation_node</tt>.
  5. Add the file <tt>vector_publisher.py</tt> available in this folder to your package.
  6. Modify the files <tt>setup.py</tt> and <tt>package.xml</tt> so that the node written in <tt>vector_publisher.py</tt> can be run with the command <tt>ros2 run tuto_1 vector_publisher</tt>.
  7. Write the content of the file <tt>rotation_node.py</tt>. The node should perform the following tasks:
        * read the vector published as a <tt>std_msgs.msg.Float32MultiArray</tt> message every 0.5 seconds on the topic <tt>bearing_vector</tt>,
        * apply a rotation of $\pi/5$ rad around the axis $\[0.707, 0.0, 0.707\]$ to the retrieved vector (hint : use the scipy library),
        * publish the rotated vector as a <tt>std_msgs.msg.Float32MultiArray</tt> message on a topic called <tt>rotated_vector</tt>.
  8. Build your package with colcon and source the setup file.
  9. Test your code by first running the command <tt>ros2 run tuto_1 vector_publisher</tt> in a terminal, and then by running the command <tt>ros2 run tuto_1 rotation_node</tt> in another terminal.
