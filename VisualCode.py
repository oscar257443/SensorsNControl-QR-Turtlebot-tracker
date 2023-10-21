import rospy
from geometry_msgs.msg import PoseStamped
from tf.transformations import quaternion_from_euler

def publish_goal(x, y, theta):
    rospy.init_node('goal_publisher', anonymous=True)
    pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz

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

    while not rospy.is_shutdown():
        pub.publish(goal)
        rate.sleep()

if __name__ == '__main__':
    try:
        x_goal = -2.0  # X position
        y_goal = -2.0  # Y position
        theta_goal = 1*1.57  # Yaw angle in radians (approximately 90 degrees)
        publish_goal(x_goal, y_goal, theta_goal)
    except rospy.ROSInterruptException:
        pass
