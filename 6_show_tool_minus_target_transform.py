#!/usr/bin/env python

#import roslib

import rospy
import tf
from math import pi


if __name__ == '__main__':
    rospy.init_node('tool_tf_broadcaster2')
    target = tf.TransformBroadcaster()
    rate = rospy.Rate(10.0)
    rospy.set_param('target/name', "vise")
    rospy.set_param('target/translation', [0.2, 0.05, 0.1])
    rospy.set_param('target/rotation', [0., 0., 0., 1.])
    while not rospy.is_shutdown():
        target_name = rospy.get_param('target/name')
        target_trans = tuple(rospy.get_param('target/translation'))
        target_rota = tuple(rospy.get_param('target/rotation'))

        #print(target_name, target_trans, target_rota)
        target.sendTransform(target_trans,
                            target_rota,
                            rospy.Time.now(),
                            "target",
                            str(target_name))
        rate.sleep()