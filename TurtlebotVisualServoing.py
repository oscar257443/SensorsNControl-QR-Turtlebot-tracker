import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import rospy
from geometry_msgs.msg import PoseStamped
import numpy as np
import math
from tf.transformations import quaternion_from_euler

reference_image = cv2.imread('reference_image.jpg')


def visual_servo(reference_img, current_img):
    # Convert images to grayscale for feature matching
    reference_gray = cv2.cvtColor(reference_img, cv2.COLOR_BGR2GRAY)
    current_gray = cv2.cvtColor(current_img, cv2.COLOR_BGR2GRAY)

    # Feature detection and matching (SIFT in this example)
    sift = cv2.SIFT_create()
    kp1, des1 = sift.detectAndCompute(reference_gray, None)
    kp2, des2 = sift.detectAndCompute(current_gray, None)

    # Feature matching
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)

    # Apply ratio test to select good matches
    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)

    # Calculate the error (difference in feature positions)
    error = np.mean([kp2[match.trainIdx].pt - kp1[match.queryIdx].pt for match in good_matches], axis=0)

    return error

# Callback function to process the ROS image message
def image_callback(msg):
    global Camerafeed  
    try:
        # ROS Image message to an OpenCV image
        Camerafeed = bridge.imgmsg_to_cv2(msg, "bgr8")

    except Exception as e:
        print(e)

def publish_goal(x, y, theta):
    rospy.init_node('goal_publisher', anonymous=True)
    pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
    

    goal = PoseStamped()
    goal.header.frame_id = "map"
    goal.pose.position.x = x
    goal.pose.position.y = y

    ## Euler to a quaternion
    quaternion = quaternion_from_euler(0, 0, theta)  # (Roll, Pitch, Yaw)

    # Set the orientation of the goal PoseStamped
    goal.pose.orientation.x = quaternion[0]
    goal.pose.orientation.y = quaternion[1]
    goal.pose.orientation.z = quaternion[2]
    goal.pose.orientation.w = quaternion[3]
    pub.publish(goal)
        
        



# Initialize ROS node
rospy.init_node('image_processing_node', anonymous=True)
# Subscribe to the ROS image topic
rospy.Subscriber("/your/image/topic", Image, image_callback)

bridge = CvBridge()
Camerafeed = None  



# def visualServoMovement(VisualServoVector):
#     # NOT FINISHED NEED TO CHANGE VisualServoVector * x to proper format ie VisualServoVector[0]
#     mvX = VisualServoVector * 0.30
#     mvY = VisualServoVector * 0.30
#     mvTheta = x = VisualServoVector * (math.pi/8)
#     publish_goal(mvX, mvY, mvTheta)
#     # Wait until ros sends finished command
#     # while(!ROSFINISHED)














if __name__ == '__main__':
    # try:
    #     x_goal = 10.0  # X position
    #     y_goal = 25.0  # Y position
    #     theta_goal = 1.57  # Yaw angle in radians (approximately 90 degrees)
    #     publish_goal(x_goal, y_goal, theta_goal)
    # except rospy.ROSInterruptException:
    #     pass
    rate = rospy.Rate(10)  # 10 Hz
    while(True):
        Vector = visual_servo(reference_image,Camerafeed)
        # if vector > threshold
        # visualServoMovement(Vector)
        # else
        # Update to new photo. IE 30cm or 1m image depending on situation.
            # reference_image = cv2.imread('reference_image2.jpg') 
        rate.sleep()


    rospy.spin()
