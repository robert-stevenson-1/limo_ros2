# 真机运行：Running on the Jetson Nano:
# 克隆仓库
```shell
# 创建本地工作目录 Create local workspace
mkdir -p ~/limo_ros2_ws/src
cd ~/limo_ros2_ws/src
# 克隆项目 Clone the project
git clone https://github.com/westonrobot/limo_ros2.git

mv limo_ros2/.devcontainer/ ..

code ..
```
[Recommend] Login the limo via VS Code Remote Development extension. 

In the workspace root folder, Crtl + Shift + P to open up the command palette, and select Remote-Containers: Rebuild and Reopen in Container``

或运行自动配置脚本 Or running automatically setup script``

```shell
cd ~/agx_workspace/src
chmod +x setup.sh
./docker_setup.sh
```
然后按照提示进行操作 Then follow the prompts

# 仿真： Simulation:
下面的脚本一条一条运行， 注意不能在后台运行  After installing ROS2 Eloquent [see documents here](docs/README.md) and setting up the software and environment run the following scripts one by one, being careful not to run in the background

# 前期准备 Preparing
```shell
# 创建本地工作目录 Create local workspace
mkdir -p ~/agx_workspace
cd ~/agx_workspace
# 克隆项目 Clone the project
git clone https://github.com/agilexrobotics/limo_ros2.git src
# 中国大陆用户加速下载(Provide accelerated downloads for users in Chinese Mainland) 
# git clone https://ghproxy.com/https://github.com/agilexrobotics/limo_ros2.git src

# 安装必要支持库 Install essential packages
apt-get update \
    && apt-get install -y --no-install-recommends \	
    libusb-1.0-0 \
    udev \
    apt-transport-https \
    ca-certificates \
    curl \
    swig \
    software-properties-common \
    python3-pip


# 安装雷达驱动 Install ydlidar driver
git clone https://ghproxy.com/https://github.com/YDLIDAR/YDLidar-SDK.git &&\
    mkdir -p YDLidar-SDK/build && \
    cd YDLidar-SDK/build &&\
    cmake ..&&\
    make &&\
    make install &&\
    cd .. &&\
    pip install . &&\
    cd .. && rm -r YDLidar-SDK 

```

# Install ROS dependencies
```shell

rosdep update
rosdep install --from-paths src --ignore-src -r -y

```

# Convenience script for compiling limo_ros2 packages
```
# do once, copy to workspace root

cp src/limo_ros2/./build.sh . 

# in workspace root
./build.sh

# Remember to always source ros workspace on new terminal
. install/setup.bash

```

# 导航 Navigation

```shell
rviz2
## 启动底盘 start the chassis
ros2 launch limo_bringup limo_start.launch.py
sleep 2

## 启动导航 start navigation
ros2 launch limo_bringup limo_navigation.launch.py
sleep 2

## 启动定位 start positioning
ros2 launch limo_bringup limo_localization.launch.py
```

# 建图 start positioning

```shell
rviz2
ros2 launch limo_bringup limo_start.launch.py
ros2 launch build_map_2d revo_build_map_2d.launch.py
#上面三条指令启动之后，用遥控器控制车子行走 After the above three command are activated use a separate screen to control the car
```


# 键盘控制 keyboard control

```shell
ros2 launch limo_bringup limo_start.launch.py
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

# 仿真 Simulation

## 四轮差速模式  Four wheel differential mode

rviz2中显示模型  Display the model in rviz2

```
ros2 launch limo_description display_models_diff.launch.py 
```

gazebo中显示模型 Run the simulation in gazebo

```
ros2 launch limo_description gazebo_models_diff.launch.py 
```

启动键盘控制节点控制limo Start keyboard teleop to control Limo

```
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

## 阿克曼模式  Ackermann Model

开发中  In development





