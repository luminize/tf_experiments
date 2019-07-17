#!/usr/bin/env python  
import time
import rospy
import tf2_ros
import moveit_commander
from moveit_commander import MoveGroupCommander
from copy import deepcopy

if __name__ == '__main__':
    rospy.init_node('carrots_listener')

    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)

    try:
        carrot2 = tfBuffer.lookup_transform('rb07_stand_link',
                                            'carrot2',
                                            rospy.Time(0),
                                            rospy.Duration(1.0))
        carrot3 = tfBuffer.lookup_transform('rb07_stand_link',
                                            'carrot3',
                                            rospy.Time(0),
                                            rospy.Duration(1.0))

    except (tf2_ros.LookupException, tf2_ros.ConnectivityException,         tf2_ros.ExtrapolationException):  
        print("Oops, something went wrong")

    #print(carrot3)
    #print(carrot2.transform)

    # get current pose
    cartesian = rospy.get_param('~cartesian', True)
    print "cartesian = %s" % cartesian            
    # Instantiate a robotcommander object
    robot = moveit_commander.RobotCommander()
    # Connect to the manipulator move group
    manipulator = MoveGroupCommander('manipulator')
    manipulator.set_planner_id("PRMkConfigDefault")
    # Allow replanning to increase the odds of a solution
    manipulator.allow_replanning(True)
    # Set the robot reference frame
    manipulator.set_pose_reference_frame('rb07_stand_link')
    # Allow some leeway in position(meters) and orientation (radians)
    manipulator.set_goal_position_tolerance(0.00001)
    manipulator.set_goal_orientation_tolerance(0.0001)
    # Get the name of the end-effector link
    end_effector_link = manipulator.get_end_effector_link()
    start_pose = manipulator.get_current_pose(end_effector_link).pose
    # go home
    manipulator.set_named_target('all-zeros')
    manipulator.go()
    rospy.sleep(1)
    # go to carrot2
    print(start_pose)
    carrot2_pose = deepcopy(start_pose)
    carrot2_pose.position.x = carrot2.transform.translation.x
    carrot2_pose.position.y = carrot2.transform.translation.y
    carrot2_pose.position.z = carrot2.transform.translation.z
    carrot2_pose.orientation.x = carrot2.transform.rotation.x
    carrot2_pose.orientation.y = carrot2.transform.rotation.y
    carrot2_pose.orientation.z = carrot2.transform.rotation.z
    carrot2_pose.orientation.w = carrot2.transform.rotation.w
    manipulator.set_pose_target(carrot2_pose)
    manipulator.go()
    time.sleep(10)
    # go home
    manipulator.set_named_target('all-zeros')
    manipulator.go()
    time.sleep(1)
    # go to carrot3
    carrot3_pose = deepcopy(start_pose)
    carrot3_pose.position.x = carrot3.transform.translation.x
    carrot3_pose.position.y = carrot3.transform.translation.y
    carrot3_pose.position.z = carrot3.transform.translation.z
    carrot3_pose.orientation.x = carrot3.transform.rotation.x
    carrot3_pose.orientation.y = carrot3.transform.rotation.y
    carrot3_pose.orientation.z = carrot3.transform.rotation.z
    carrot3_pose.orientation.w = carrot3.transform.rotation.w
    manipulator.set_pose_target(carrot3_pose)
    manipulator.go()