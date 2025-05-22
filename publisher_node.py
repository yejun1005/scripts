import rospy
from std_msgs.msg import String

rospy.init_node('publisher_node')
rospy.loginfo('publisher node started. now publish message')
pub = rospy.Publisher('talking_topic', String, queue_size = 10)
rate = rospy.Rate(2)

while not rospy.is_shutdown():
    pub.publish('call me please')
    rate.sleep()
