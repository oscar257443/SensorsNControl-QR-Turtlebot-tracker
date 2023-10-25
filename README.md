# SensorsNControl-QR-Turtlebot-tracker

## Individual Contribution
Quoc Minh Tran SID 12853305 40%

Oscar Gullickson SID 13558578  30%

Ben Thomas SID 13973108 30%


## Code Description
### Enviroment


### Slam and Pathplanning

### Python scripts
There is a total of 4 python scripts. 
I created 3 pieces of code that each served a difference purpose and then integrated them into a singular functional piece of code, called TurtlebotVisualServoing.py, that combined the 3.  This code does not function as one of the subcodes was not able to be completed , Visual servoing, in time for submission therefore the control systems are not working.

The sub codes are VisualServoing.py, VisualCode.py, and ROS2CV2.py. 

The ROS2CV2.py  involved subscribe the camera data and importing it to the python environment for further processing. This is working as intended

The VisualCode.py involved creating a publishing node that gives the next position for the robot to move to in the visual servoing method. This works by creating a rostopic and node and transforming a x y theta input to the function to the posestamp format desired by the rospackage. We also have to change the euler angle to a quaternion format in order to meet the requirements of the format. Then we publish the goal and the path planning works as intended. This is working as intended.

The VisualServoing.py this part I worked on was the detection and then visual servoing. This grabs the images then proceeds to use orb feature detection and brute force matching to get matching pair. Then we filter the pair in order to get the good pairs. This is where we stop as we wasnt able to perform the calculations due to python inexperience combined with lack of time remaining 

Required packages for the python scripts:
    pip install roslibpy
    pip install opencv-python==4.7.0.68
