from lib import roboconnect
import math

robot = roboconnect.Connect(['motion', 'posture'])

# Makes the robot stand up, walk forward 50 centermetres, turn around
# walk back to where it came from, turn around, and sit down.
# Make sure there is nothing in its way!

robot.api['posture'].goToPosture('Stand', 0.5)

ONE_HUNDRED_EIGHTY_DEGREES = math.pi

for i in range(0, 2):
    robot.api['motion'].moveTo(0.5, 0.0, 0, robot.stable)
    robot.api['motion'].moveTo(0.0, 0.0, ONE_HUNDRED_EIGHTY_DEGREES, robot.stable)

robot.api['posture'].goToPosture('Sit', 1.0)
