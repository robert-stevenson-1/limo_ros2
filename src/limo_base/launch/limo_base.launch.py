import os
from pyexpat import model
import launch
import launch_ros

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    model_path = os.path.join(get_package_share_directory('limo_description'),
                            'urdf', 'limo_four_diff.xacro')

    port_name_arg = DeclareLaunchArgument('port_name', default_value='ttyTHS1',
                                          description='usb bus name, e.g. ttyTHS1')
    odom_frame_arg = DeclareLaunchArgument('odom_frame', default_value='odom',
                                           description='Odometry frame id')
    base_link_frame_arg = DeclareLaunchArgument('base_frame', default_value='base_link',
                                                description='Base link frame id')
    odom_topic_arg = DeclareLaunchArgument('odom_topic_name', default_value='odom',
                                           description='Odometry topic name')
    sim_control_rate_arg = DeclareLaunchArgument('control_rate', default_value='50',
                                                 description='Simulation control loop update rate')
    use_mcnamu_arg = DeclareLaunchArgument('use_mcnamu', default_value='false',
                                           description='Use mecanum motion mode')

    limo_base_node = launch_ros.actions.Node(
        package='limo_base',
        executable='limo_base',
        output='screen',
        emulate_tty=True,
        parameters=[{
                'port_name': launch.substitutions.LaunchConfiguration('port_name'),
                'odom_frame': launch.substitutions.LaunchConfiguration('odom_frame'),
                'base_frame': launch.substitutions.LaunchConfiguration('base_frame'),
                'odom_topic_name': launch.substitutions.LaunchConfiguration('odom_topic_name'),
                'control_rate': launch.substitutions.LaunchConfiguration('control_rate'),
                'use_mcnamu': launch.substitutions.LaunchConfiguration('use_mcnamu'),
        }])

    limo_joint_state_node = launch_ros.actions.Node(
        package='joint_state_publisher',
        executable='joint_state_publisher'
    )
    limo_robot_state_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': Command(['xacro ', model_path])}]
    )

    return LaunchDescription([
        port_name_arg,
        odom_frame_arg,
        base_link_frame_arg,
        odom_topic_arg,
        sim_control_rate_arg,
        use_mcnamu_arg,
        limo_base_node,
        limo_joint_state_node,
        limo_robot_state_node
    ])
