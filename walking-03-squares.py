from lib import roboconnect
import math

robot = roboconnect.Connect(['motion', 'posture'])

# Makes the robot walk in a square, with each edge being around 50 centermetres
# in length.
# Make sure there is nothing in its way!

robot.api['posture'].goToPosture('Stand', 0.5)

NINETY_DEGREES = (math.pi / 2)

for i in range(0, 4):
    robot.api['motion'].moveTo(0.5, 0.0, 0, robot.stable)
    robot.api['motion'].moveTo(0.0, 0.0, NINETY_DEGREES, robot.stable)

robot.api['posture'].goToPosture('Sit', 1.0)
