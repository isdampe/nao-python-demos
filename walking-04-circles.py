from lib import roboconnect
import math

robot = roboconnect.Connect(['motion', 'posture'])

# Makes the robot walk in a circle with a radius of approx. 50 centermetres
# Make sure there is nothing in its way!

robot.api['posture'].goToPosture('Stand', 0.5)

for i in range(0, 4):
    robot.api['motion'].moveTo(0.5, 0.5, (math.pi /2), robot.stable)

robot.api['posture'].goToPosture('Sit', 1.0)
