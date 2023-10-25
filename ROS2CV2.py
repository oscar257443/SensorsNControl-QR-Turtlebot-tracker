import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import rospy
Camerafeed = None
# Initialize ROS node
rospy.init_node('image_processing_node', anonymous=True)

# Create a CvBridge object
bridge = CvBridge()

# Define a callback function to process the ROS image message
def image_callback(msg):
    try:
        global Camerafeed  
        # Convert the ROS Image message to an OpenCV image
        Camerafeed = bridge.imgmsg_to_cv2(msg, "bgr8")
        
    except Exception as e:
        print(e)

# Subscribe to the ROS image topic
rospy.Subscriber("/camera/raw", Image, image_callback)

# Spin to keep the script running
rospy.spin()
