#!/usr/bin/env python

#import roslib

import rospy
import tf
from math import pi
from tf.transformations import *

if __name__ == '__main__':
    rospy.init_node('robot_tool_tf_broadcaster')
    tool = tf.TransformBroadcaster()
    rate = rospy.Rate(10.0)
    vise_q_orig = quaternion_from_euler(0, 0, 0)
    #vise_q_rot = quaternion_from_euler(pi/2, pi/2, 0.)
    #vise_q_new = quaternion_multiply(vise_q_rot, vise_q_orig)
    r = vise_q_orig
    rospy.set_param('tool/name', "tooltip")
    rospy.set_param('tool/translation', [0.05, 0.05, -0.1])
    rospy.set_param('tool/rotation', [0., 0., 0., 1.])
    while not rospy.is_shutdown():
        name = rospy.get_param('tool/name')
        trans = tuple(rospy.get_param('tool/translation'))
        rota = tuple(rospy.get_param('tool/rotation'))
        tool.sendTransform(trans,
                         rota,
                         rospy.Time.now(),
                         name,
                         "tool0")
        rate.sleep()