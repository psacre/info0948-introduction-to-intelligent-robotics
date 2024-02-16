# PC setup
This folder is dedicated to the installation of the virtual machine on which ROS2 and Gazebo are already installed. ROS2 foxy works on the Ubuntu Focal Fossa 20.04 operating system. Follow the instructions related to your operating system. 

(*Source: Those instructions are taken from [Mathworks](https://fr.mathworks.com/support/product/robotics/ros2-vm-installation-instructions-v6.html).*)

#### Windows (64-bit)
  1. Download and install the [VMware® Player software](https://www.vmware.com/go/getplayer-win).
  2. Download the [archive](https://mseduculiegebe-my.sharepoint.com/:u:/g/personal/sven_goffin_uliege_be/EcEvyeZmyP5Ek__h_FnzKEQBoXNf-VZzsrb38fgaM5P-Uw?e=a9SivD) containing the virtual machine.
  3. Decompress the archive to a location on your hard drive.
  4. Start VMware Player.
  5. In VMware Player, press **Open a Virtual Machine**.
  6. Browse to the location of the Ubuntu image, select the **vm_ros_foxy.vmx** file and press **OK**.
  7. The virtual machine is now added to your library.
  8. Press **Edit virtual machine settings** and specify the amount of memory (RAM) for this virtual machine. We recommend at least 4Go RAM.
  9. In VMware Player, start the virtual machine.
  10. Press **I copied it** if a window opens that asks if you copied or moved the virtual machine.

#### Linux (64-bit)
  1. Download the [VMware® Player software](https://www.vmware.com/go/getplayer-linux) bundle.
  2. Install VMware Player by executing the bundle installer with administrative privileges.
  3. Download the [archive](https://mseduculiegebe-my.sharepoint.com/:u:/g/personal/sven_goffin_uliege_be/EcEvyeZmyP5Ek__h_FnzKEQBoXNf-VZzsrb38fgaM5P-Uw?e=a9SivD) containing the virtual machine.
  4. Decompress the archive to a location on your hard drive.
  5. Start VMware Player.
  6. In VMware Player, press **Open a Virtual Machine**.
  7. Browse to the location of the Ubuntu image, select the **vm_ros_foxy.vmx** file and press **OK**.
  8. The virtual machine is now added to your library.
  8. Press **Edit virtual machine settings** and specify the amount of memory (RAM) for this virtual machine. We recommend at least 4Go RAM.
  9. In VMware Player, start the virtual machine.
  10. Press **I copied it** if a window opens that asks if you copied or moved the virtual machine.

#### Mac OS X - Intel hosts (64-bit)
  1. Create an account for personal use on the [VMWare® Fusion website](https://customerconnect.vmware.com/account-registration).
  2. Log in to your new account.
  3. Download and install [VMWare® Fusion](https://customerconnect.vmware.com/evalcenter?p=fusion-player-personal-13) for **Intel hosts**.
  4. Download the [archive](https://mseduculiegebe-my.sharepoint.com/:u:/g/personal/sven_goffin_uliege_be/EcEvyeZmyP5Ek__h_FnzKEQBoXNf-VZzsrb38fgaM5P-Uw?e=a9SivD) containing the virtual machine.
  5. Decompress the archive to a location on your hard drive.
  6. Start VMware Player.
  7. In VMware Player, press **Open a Virtual Machine**.
  8. Browse to the location of the Ubuntu image, select the **vm_ros_foxy.vmx** file and press **OK**.
  9. The virtual machine is now added to your library.
  10. Press **Edit virtual machine settings** and specify the amount of memory (RAM) for this virtual machine. We recommend at least 4Go RAM.
  11. In VMware Player, start the virtual machine.
  12. Press **I copied it** if a window opens that asks if you copied or moved the virtual machine.


#### Mac OS X - Arm64 (M1/M2/M3) hosts (64-bit)
  1. Create an account for personal use on the [VMWare® Fusion website](https://customerconnect.vmware.com/account-registration).
  2. Log in to your new account.
  3. Download and install [VMWare® Fusion](https://customerconnect.vmware.com/evalcenter?p=fusion-player-personal-13) for **Arm64 (M1/M2) hosts**.
  4. Download the [archive]() containing the virtual machine.
  5. Decompress the archive to a location on your hard drive.
  6. Start VMware Player.
  7. In VMware Player, press **Open a Virtual Machine**.
  8. Browse to the location of the Ubuntu image, select the **vm_ros_foxy.vmx** file and press **OK**.
  9. The virtual machine is now added to your library.
  10. Press **Edit virtual machine settings** and specify the amount of memory (RAM) for this virtual machine. We recommend at least 4Go RAM.
  11. In VMware Player, start the virtual machine.
  12. Press **I copied it** if a window opens that asks if you copied or moved the virtual machine.

# Using the virtual machine
When you start the virtual machine with VMWare, a window with Linux running will pop up. You can open the terminal with the shortcut `Ctrl + Alt + T`. This terminal is a bash terminal with ROS2 and Gazebo installed.
