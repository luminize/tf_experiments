# rosservice call /hal_402_drives_mgr "started"
# ./mill-user-coordinate-systempy &
# ./robot_tool_tf_broadcaster.py &

import rospy
import tf

rospy.init_node('some_node')
target = tf.TransformBroadcaster()
target.sendTransform((0.2, 0.05, 0.1),(0,0,0,1),rospy.Time.now(), "target", "vise")

# start new terminal
# ./3_show_tool_minus_target_transform.py

rospy.set_param('target/translation', [0.1, 0.1, 0.2])

# ./4_move_to_vise_tool0_tf