from lib import roboconnect

robot = roboconnect.Connect(['motion', 'posture'])

# Makes the robot stand up, walk forward 50 centermetres, and sit down.
# Make sure there is nothing in its way!
robot.api['posture'].goToPosture('Stand', 0.5)
robot.api['motion'].moveTo(0.5, 0, 0)
robot.api['posture'].goToPosture('Sit', 1.0)
