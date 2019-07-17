
#!/bin/bash -e

./replace_tool0_frame.py
rosnode kill /robot_state_publisher
rosrun robot_state_publisher robot_state_publisher robot_state_publisher &
