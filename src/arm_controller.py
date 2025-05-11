#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def move_arm():
    rospy.init_node('arm_controller', anonymous=True)
    pub = rospy.Publisher('/arm_movement', String, queue_size=10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        command = "move_forward"
        pub.publish(command)
        rate.sleep()

if __name__ == '__main__':
    try:
        move_arm()
    except rospy.ROSInterruptException:
        pass
