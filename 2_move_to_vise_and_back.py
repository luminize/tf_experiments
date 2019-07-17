#!/usr/bin/env python  
import time
import rospy
import tf2_ros
import moveit_commander
from moveit_commander import MoveGroupCommander
from copy import deepcopy


def set_target(pose, transform):
    pose.position.x = transform.transform.translation.x
    pose.position.y = transform.transform.translation.y
    pose.position.z = transform.transform.translation.z
    pose.orientation.x = transform.transform.rotation.x
    pose.orientation.y = transform.transform.rotation.y
    pose.orientation.z = transform.transform.rotation.z
    pose.orientation.w = transform.transform.rotation.w
    return pose


def get_transform(name):
    try:
        tf_ = tfBuffer.lookup_transform('rb07_stand_link',
                                            name,
                                            rospy.Time(0),
                                            rospy.Duration(1.0))

    except (tf2_ros.LookupException, tf2_ros.ConnectivityException,         tf2_ros.ExtrapolationException):  
        print("Oops, something went wrong")
    return tf_


def go_to_pose(name, manipulator, start_pose):
    pose = deepcopy(start_pose)
    tf_ = get_transform(name)
    pose = set_target(pose, tf_)
    manipulator.set_pose_target(pose)
    print("go to %s" % name)
    manipulator.go()
    print("wait for 2 seconds")
    time.sleep(2)


if __name__ == '__main__':
    rospy.init_node('vise_listener')

    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)

    # Instantiate a robotcommander object
    robot = moveit_commander.RobotCommander()
    # Connect to the manipulator move group and get end effector link
    manipulator = MoveGroupCommander('manipulator')
    end_effector_link = manipulator.get_end_effector_link()
    # Set the robot reference frame
    manipulator.set_pose_reference_frame('rb07_stand_link')
    # Allow replanning to increase the odds of a solution
    manipulator.allow_replanning(True)
    # Set accuracy in position(meters) and orientation (radians)
    manipulator.set_goal_position_tolerance(0.00001)
    manipulator.set_goal_orientation_tolerance(0.0001)
    
    manipulator.set_planner_id("RRTkConfigDefault")
    
    # Get a pose to modify
    start_pose = manipulator.get_current_pose(end_effector_link).pose
    
    # go home
    manipulator.set_named_target('all-zeros')
    manipulator.go()
    rospy.sleep(1)
    # go to vise
    go_to_pose('vise', manipulator, start_pose)
    # go to g54
    go_to_pose('G54', manipulator, start_pose)
    # go to g55
    go_to_pose('G55', manipulator, start_pose)
    # go to vise
    go_to_pose('vise', manipulator, start_pose)

    # go home
    manipulator.set_named_target('all-zeros')
    manipulator.go()
    time.sleep(1)
