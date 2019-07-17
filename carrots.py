#!/usr/bin/env python
import roslib
#roslib.load_manifest('learning_tf')

import rospy
import tf
from tf.transformations import *

if __name__ == '__main__':
    rospy.init_node('fixed_tf_broadcaster')
    c1 = tf.TransformBroadcaster()
    c2 = tf.TransformBroadcaster()
    c3 = tf.TransformBroadcaster()
    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        c1.sendTransform((0.1, 0.2, 0.1),
                         (0.0, 0.0, 0.0, 1.0),
                         rospy.Time.now(),
                         "carrot1",
                         "flange")
        c2.sendTransform((0.5, 0.5, 0.5),
                    (0.0, 0.0, 0.0, 1.0),
                    rospy.Time.now(),
                    "carrot2",
                    "rb07_stand_flange")
        q_orig = quaternion_from_euler(0, 0, 0)
        q_rot = quaternion_from_euler(1., 1., 1.)
        q_new = quaternion_multiply(q_rot, q_orig)
        c3.sendTransform((0.0, 0.5, -0.2),
                    q_new,
                    rospy.Time.now(),
                    "carrot3",
                    "rb07_stand_flange")
        rate.sleep()