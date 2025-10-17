from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='jan_fwl',
            executable='temp_sensor_node',
            name='temp_sensor',
            output='screen'
        ),
        Node(
            package='jan_fwl',
            executable='alert_node',
            name='alert_node',
            output='screen'
        ),
    ])
