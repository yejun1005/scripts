import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo("received data: %s", msg.data)
    
def listener():
    rospy.init_node('Subscriber_Node', anonymous=True)
    rospy.Subscriber('talking_topic', String, callback)
    rospy.spin()

if __name__ == "__main__":
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
