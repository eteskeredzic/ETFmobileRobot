# ETFmobileRobot
A mobile robot for autonomous exploration and obstacle avoidance in urban search and rescue environments using the Hector software stack. This robot uses only one external sensor (a lidar sensor) and requires no odometry source (such as wheel encoders). However, it can only be used on flat surfaces (unless and IMU is incorporated into the system). 

## Getting the code

To download all the relevant code used in the implementation of this mobile robot platform, you must first clone this github repository. You can do that with the command `git clone https://github.com/eteskeredzic/ETFmobileRobot`

After that, in the folder labled _src_ you can find all the relevant code. The folder is divided into subfolders, as follows:

- *RPLidar_Hector_SLAM* folder, which contains the ROS node for the RPLidar sensor, as well as all the scripts to run Hector SLAM, which does mapping and localization;
- *hector_navigation* folder, which contains all scripts to run navigation;
- *MotorController* folder, which contains scripts for controlling the motors, that is, driving the robot. Each script contains a short comment on exactly what it does;
- *key_teleop* folder, which is used for driving the robot manually;

## Launching

After building the workspace, you can run all relevant parts of the system. In the main folder of the workspace, there are multiple BASH scripts, which can be used for automatic launch. To launch the robot, simply run the script `0.sh` through the terminal. Alternatively, if you want to run the system manually, you need to launch the following commands (in seperate terminals):

```
roslaunch rplidar_ros rplidar.launch
roslaunch hector_slam tutorial.launch
roslaunch nav.launch
rosrun hector_exploration_controller simple_exploration_controller
rosrun MotorController newController.py
```
Don't forget to 'source devel/setup.bash'.

To launch the system for manual control of the robot, use the command `rosrun key_teleop key_teleop.py`

## Modifying parameters:

Multiple parameters are available for modificitaion, with the most important being:

- *hector_navigation/hector_exploration_node/config/costmap.yaml* is a file which containts all the parameters for the costmap. It is important to modify those parameters to fit the mobile platform that you are using;
- *hector_navigation/hector_exploration_controller/src/simple_exploration_controller.cpp* containts timers for calling the exploration service, as well as sending velocity commands. Those timers (which are 15 seconds and 0.1 seconds by default) can be modified through the variables `exploration_plan_generation_timer_` and `cmd_vel_generator_timer_`;
- *hector_navigation/hector_path_follower/src/hector_path_follower.cpp* containts several parameters. These parameters are: `tolerance_trans` (allowed error for linear movement), `tolerance_rot` (allowed error for angular movement), `max_vel_lin` (maximum linear velocity), `max_vel_th` (maximum angular velocity), `min_vel_lin` (minimum linear velocity), `min_vel_th` (minimum angular velocity);
- *RPLidar_Hector_SLAM/hector_slam/hector_mapping/launch/mapping_demo.launch* containts parameters for environment mapping. It is recommeneded to keep the parameter `map_size` on values no greater than 1024. The map update parameters should be setup in accordance to the specifications of the lidar sensor you are using; 

## Example:
 ![First floor of the Faculty of Electrical Engineering in Sarajevo](https://raw.githubusercontent.com/eteskeredzic/ETFmobileRobot/master/floormap.png)
 
First floor of the Faculty of Electrical Engineering in Sarajevo

## External links:

- [Hector SLAM](http://wiki.ros.org/hector_slam)
- [Hector Navigation](http://wiki.ros.org/hector_navigation)
