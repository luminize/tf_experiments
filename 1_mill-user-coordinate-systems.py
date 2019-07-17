#!/usr/bin/env python

import rospy
import tf
from math import pi
from tf.transformations import *

if __name__ == '__main__':
    rospy.init_node('fixed_tf_broadcaster')
    vise = tf.TransformBroadcaster()
    g54 = tf.TransformBroadcaster()
    g55 = tf.TransformBroadcaster()
    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        vise_q_orig = quaternion_from_euler(0, 0, 0)
        #vise_q_rot = quaternion_from_euler(pi/2, pi/2, 0.)
        #vise_q_new = quaternion_multiply(vise_q_rot, vise_q_orig)
        vise_q_rot = vise_q_orig
        vise.sendTransform((0.2, 0.05, 0.1),
                         vise_q_rot,
                         rospy.Time.now(),
                         "vise",
                         "x_axis")
        g54.sendTransform((0.2, 0.1, 1.),
                    vise_q_rot,
                    rospy.Time.now(),
                    "G54",
                    "frame")
        g55.sendTransform((0.2, -0.1, 1.1),
                    vise_q_rot,
                    rospy.Time.now(),
                    "G55",
                    "frame")
        rate.sleep()