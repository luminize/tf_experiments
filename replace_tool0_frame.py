#!/usr/bin/env python
import rospy

# load the entire loaded URDF
description = rospy.get_param('robot_description')

# find marker
character_first = description.find("<!-- marker -->")

# find position of tf coordinates after marker
old_coord_pos_str = 'xyz='
character_first = description.find(old_coord_pos_str, character_first)
character_first = description.find('"', character_first) + 1
character_last = description.find('"', character_first)

new_pos = "0. 0. 0."

first_part_urdf = description[:character_first]
last_part_urdf = description[character_last:]

new_urdf = first_part_urdf + new_pos + last_part_urdf

rospy.set_param('robot_description', new_urdf)