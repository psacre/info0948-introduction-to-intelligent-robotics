### Homework
The goal of this homework is to apply the concepts you learned during the first tutorial. You have to create a ROS2 package that contains a node that retrieves a vector from a topic, rotates it around a given axis, and publishes the result on another topic. To do so, follow the procedure below:
  1. Create a workspace called <tt>tutorials_ws<tt>.
  2. Within this workspace, create a package called <tt>tuto_1<tt>.
  3. Create a python file <tt>rotation_node.py<tt> in the appropriate folder of your package <tt>tuto_1<tt>.
  4. Modify the files <tt>setup.py<tt> and <tt>package.xml<tt> so that the node you will write in <tt>rotation_node.py<tt> can be run with the command <tt>ros2 run tuto_1 rotation_node<tt>.
  5. Add the file <tt>vector_publisher.py<tt> available in this folder to your package.
  6. Modify the files <tt>setup.py<tt> and <tt>package.xml<tt> so that the node written in <tt>vector_publisher.py<tt> can be run with the command <tt>ros2 run tuto_1 vector_publisher<tt>.
  7. Write the content of the file <tt>rotation_node.py<tt>. The node should perform the following tasks:
        * read the vector published as a <tt>std_msgs.msg.Float32MultiArray<tt> message every 0.5 seconds on the topic <tt>bearing_vector<tt>,
        * apply a rotation of $\pi/5$ rad around the axis $\[0.707, 0.0, 0.707\]$ to the retrieved vector (hint : use the scipy library),
        * publish the rotated vector as a <tt>std_msgs.msg.Float32MultiArray<tt> message on a topic called <tt>rotated_vector<tt>.
  8. Build your package with colcon and source the setup file.
  9. Test your code by first running the command <tt>ros2 run tuto_1 vector_publisher<tt> in a terminal, and then by running the command <tt>ros2 run tuto_1 rotation_node<tt> in another terminal.
