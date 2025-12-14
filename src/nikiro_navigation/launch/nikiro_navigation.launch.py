import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    use_sim_time = LaunchConfiguration("use_sim_time", default="True")
    map_dir = LaunchConfiguration(
        "map",
        default=os.path.join(
            get_package_share_directory(
                "nikiro_navigation"), "maps", "map.yaml"
        ),
    )
    param_dir = LaunchConfiguration(
        "params_file",
        default=os.path.join(
            get_package_share_directory(
                "nikiro_navigation"), "params", "nikiro_amr_params.yaml"
        ),
    )
    nav2_bringup_launch_dir = os.path.join(
        get_package_share_directory("nav2_bringup"), "launch")

    rviz_config_dir = os.path.join(get_package_share_directory(
        "nikiro_navigation"), "rviz2", "nikiro_navigation.rviz")

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "map", default_value=map_dir),
            DeclareLaunchArgument(
                "params_file", default_value=param_dir
            ),
            DeclareLaunchArgument(
                "use_sim_time", default_value="true"
            ),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(os.path.join(
                    nav2_bringup_launch_dir, "rviz_launch.py")),
                launch_arguments={
                    "namespace": "", "use_namespace": "False", "rviz_config": rviz_config_dir}.items(),
            ),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    [nav2_bringup_launch_dir, "/bringup_launch.py"]),
                launch_arguments={
                    "map": map_dir, "use_sim_time": use_sim_time, "params_file": param_dir}.items(),
            ),
        ]
    )
