import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import rospy

# Initialize ROS node
rospy.init_node('image_processing_node', anonymous=True)

# Create a CvBridge object
bridge = CvBridge()

# Define a callback function to process the ROS image message
def image_callback(msg):
    try:
        # Convert the ROS Image message to an OpenCV image
        cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")
        
        # Now you can work with the OpenCV image (cv_image) here
        # For example, you can display it using cv2.imshow() or perform image processing.

    except Exception as e:
        print(e)

# Subscribe to the ROS image topic
rospy.Subscriber("/your/image/topic", Image, image_callback)

# Spin to keep the script running
rospy.spin()
