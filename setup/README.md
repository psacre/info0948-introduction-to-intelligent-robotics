# Virtual machine setup
This folder is dedicated to the installation of the virtual machine on which ROS2 and Gazebo are installed. Follow the instructions related to your operating system. Those instructions are taken from [Mathworks](https://fr.mathworks.com/support/product/robotics/ros2-vm-installation-instructions-v6.html).

#### Windows (64-bit)
  1. Download and install the [VMware® Player software](https://www.vmware.com/go/getplayer-win).
  2. Download the [archive](https://ssd.mathworks.com/supportfiles/ros/virtual_machines/v3/ros_noetic_foxy_gazebov11_linux_win_v1.zip) containing the virtual machine.
  3. Decompress the archive to a location on your hard drive.
  4. Start VMware Player.
  5. In VMware Player, press **Open a Virtual Machine**.
  6. Browse to the location of the Ubuntu image, select the ros_noetic_foxy_gazebov11.vmx file and press **OK**.
  7. The virtual machine is now added to your library.
  8. In VMware Player, start the virtual machine.
  9. Press **I copied it** if a window opens that asks if you copied or moved the virtual machine.

#### Linux (64-bit)
  1. Download the [VMware® Player software](https://www.vmware.com/go/getplayer-linux) bundle.
  2. Install VMware Player by executing the bundle installer with administrative privileges.
  3. Download the [archive](https://ssd.mathworks.com/supportfiles/ros/virtual_machines/v3/ros_noetic_foxy_gazebov11_linux_win_v1.zip) containing the virtual machine.
  4. Decompress the archive to a location on your hard drive.
  5. Start VMware Player.
  6. In VMware Player, press **Open a Virtual Machine**.
  7. Browse to the location of the Ubuntu image, select the ros_noetic_foxy_gazebov11.vmx file and press **OK**.
  8. The virtual machine is now added to your library.
  9. In VMware Player, start the virtual machine.
  10. Press **I copied it** if a window opens that asks if you copied or moved the virtual machine.

#### Mac OS X - Intel hosts (64-bit)
  1. Download and install [VirtualBox®](https://download.virtualbox.org/virtualbox/6.1.26/VirtualBox-6.1.26-145957-OSX.dmg) for Intel hosts.
  2. Download the [virtual machine](https://ssd.mathworks.com/supportfiles/ros/virtual_machines/v3/ros_noetic_foxy_gazebov11_mac_v1.ova) to a folder on your hard drive.
  3. Start VirtualBox.
  4. In VirtualBox, select the **Import Appliance** entry in the **File** menu.
  5. Select the file you just downloaded and press **Next**.
  6. Verify the virtual machine settings and press **Import**. The import process might take a few minutes.
  7. The virtual machine is now added to your library.
  8. In VirtualBox, start the virtual machine.
  9. Depending on your host's network configuration, you might have to adjust the network settings of the virtual machine.     10. If on first start, the virtual machine displays a warning that a network interface was not found, press **Change Network Settings** and select the **Name** of your host's primary network adapter.


#### Mac OS X - Arm64 (M1/M2) hosts (64-bit)
  1. Download and install [VirtualBox®](https://download.virtualbox.org/virtualbox/7.0.8/VirtualBox-7.0.8_BETA4-156879-macOSArm64.dmg) for Arm64 (M1/M2) hosts. Note this is a Beta version of an outdated version of VirtualBox (the current version does not support the M1/M2 architecture).
  2. Download the [virtual machine](https://ssd.mathworks.com/supportfiles/ros/virtual_machines/v3/ros_noetic_foxy_gazebov11_mac_v1.ova) to a folder on your hard drive.
  3. Start VirtualBox.
  4. In VirtualBox, select the **Import Appliance** entry in the **File** menu.
  5. Select the file you just downloaded and press **Next**.
  6. Verify the virtual machine settings and press **Import**. The import process might take a few minutes.
  7. The virtual machine is now added to your library.
  8. In VirtualBox, start the virtual machine.
  9. Depending on your host's network configuration, you might have to adjust the network settings of the virtual machine.     10. If on first start, the virtual machine displays a warning that a network interface was not found, press **Change Network Settings** and select the **Name** of your host's primary network adapter.

# Use of the virtual machine
When you start the virtual machine with VMWare or VirtualBox, a window with Linux running will pop up. On the desktop, you will find many shortcuts. One of them is called **ROS2 foxy terminal**. This shortcut will open a terminal with ROS2 foxy and Gazebo installed. Note that opening the terminal with the shortcut Ctrl + alt + T will open a terminal that DO NOT have ROS2 and Gazebo installed. The other shortcuts won't be usefull for this course.
