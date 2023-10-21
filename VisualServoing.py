import cv2
import numpy as np

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

# Load reference and current images
reference_image = cv2.imread('reference_image.jpg')
current_image = cv2.imread('current_image.jpg')

# Calculate the error
error_vector = visual_servo(reference_image, current_image)

print("Error Vector:", error_vector)
