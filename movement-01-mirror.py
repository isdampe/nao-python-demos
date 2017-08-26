from lib import roboconnect
import time

robot = roboconnect.Connect(['motion', 'posture', 'tts'])

# Loosens the robot's right arm, reads in sensor data, and mirrors it's
# left arm to match the movement of the right arm.

# Make sure we are sitting down for this one.
robot.api['posture'].goToPosture('Sit', 0.5)
origStiff = robot.api['motion'].getStiffnesses(robot.rightArm)

# Loosen the right arm.
robot.api['motion'].setStiffnesses(robot.rightArm, 0.0)

robot.api['tts'].say('I am ready!')
robot.api['tts'].say('Gently move my right arm around!')

# Run for twenty seconds
timer = 0
while timer < 200:
    rightArmValues = robot.api['motion'].getAngles(robot.rightArm, True)
    invertedValues = robot.invertAngles(rightArmValues)
    robot.api['motion'].setAngles(robot.leftArm, invertedValues, 0.5)
    timer += 1
    time.sleep(0.1)

robot.api['tts'].say('OK!')
robot.api['tts'].say('Please let go of my arm now!')
time.sleep(5)

robot.api['motion'].setStiffnesses(robot.rightArm, origStiff)
robot.api['posture'].goToPosture('Sit', 0.5)
