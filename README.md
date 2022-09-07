# LIMO ROS 2

## [Documentation](https://github.com/agilexrobotics/limo-doc)

## Setup
### Clone the repo
```bash
git clone https://github.com/westonrobot/limo_ros2.git
```
## Login the limo via VS Code Remote Development extension [(More info here)](./docs/README.md)

1. Launch VS Code
2. SSH into limo and open workspace folder
3. In the workspace root folder, Crtl + Shift + P to open up the command palette, and select Remote-Containers: Rebuild and Reopen in Container

## Convenience script for compiling limo_ros2 packages
```bash
# in workspace root
./build.sh

# Remember to always source ros workspace on new terminal
. install/setup.bash
```

## Bringup robot

```bash
# Bringup robot
ros2 launch limo_bringup limo_start.launch.py

# OR

# Bringup robot in simulator
# Add use_sim_time:=true argument for subsequent launches if using sim
ros2 launch limo_gazebosim limo_gazebo_diff.launch.py
```

## Bringup camera

```bash
ros2 launch astra_camera dabai.launch.py
```

## Teleoperation
```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

## SLAM
```bash
# Launch SLAM node
ros2 launch limo_bringup cartographer.launch.py

# To save map
ros2 run nav2_map_server map_saver_cli -f [filename]
```


## Navigation

```bash
# In seperate terminals
ros2 launch limo_navigation limo_localization.launch.py

ros2 launch limo_navigation limo_controller.launch.py

# Single launch
ros2 launch limo_navigation limo_navigation.launch.py
```