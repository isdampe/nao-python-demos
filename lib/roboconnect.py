import sys

# Naoqi SDK imports
from naoqi import ALBroker, ALProxy

class Connect:

    def __init__(self, proxyList):
        if len(sys.argv) < 3:
            print "Invalid syntax for roboconnect"
            print "Syntax: python script.py [hostname] [port]"
            sys.exit(1)

        self.host = sys.argv[1]
        self.port = int(sys.argv[2])
        self.api = {}

        # Stable walking
        self.stable = [
            ['MaxStepX', 0.06],
            ['MaxStepY', 0.11],
            ['MaxStepTheta', 0.15],
            ['MaxStepFrequency', 0.2]
        ]

        self.leftArm   = ['LShoulderPitch', 'LShoulderRoll', 'LElbowYaw', 'LElbowRoll']
        self.rightArm = ['RShoulderPitch', 'RShoulderRoll', 'RElbowYaw', 'RElbowRoll']

        self.connectToProxies(proxyList)


    def connectToProxies(self, proxyList):
        supportedProxies = {
            'motion': 'ALMotion',
            'posture': 'ALRobotPosture',
            'memory': 'ALMemory',
            'tts': 'ALTextToSpeech',
            'camera': 'ALVideoDevice',
            'audio': 'ALAudioPlayer',
            'leds': 'ALLeds',
            'video': 'ALVideoDevice',
            'sonar': 'ALSonar'
        }

        for key in proxyList:
            if key in supportedProxies:
                self.api[key] = ALProxy(supportedProxies[key], self.host, self.port)
            else:
                print "No proxy method for " + key + " found. Skipping."

    def invertAngles(self, values):
        values[1] = -values[1]
        values[2] = -values[2]
        values[3] = -values[3]
        return values
