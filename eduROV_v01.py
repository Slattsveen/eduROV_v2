import sys, pygame, pygame.camera, os, time, serial
from sense_hat import SenseHat
# to add the piCam to the list of available cameras, run command:
# sudo modprobe bcm2835-v4l2
os.system("sudo modprobe bcm2835-v4l2")

#ititiating pygame module, camera, serial port, senseHat
pygame.init()
pygame.camera.init()
senseHat = SenseHat()
ser = serial.Serial('/dev/ttyACM0', 115200)
ser.close()
ser.open()
FPS = 35 #image updating frequenzy
fpsClock = pygame.time.Clock()
imgCounter = 0 #counter variable for numbering still frames taken during mission

width, height = 900, 600
picWidth, picHeight = 600, 400

#sensor variables, internally and externally of the ROV hull
tempROV = senseHat.get_temperature()
pressureROV = senseHat.get_pressure()
bearingROV = senseHat.get_compass() #gives compas bearing in degrees from North
humidityROV = senseHat.get_humidity()
orientationROV = senseHat.get_orientation() #a dict containgin values with tags 'pitch', 'roll', 'yaw'
batteryVoltage = 0
tempWater = 0
pressureWater = 0

motorStates = "000" #each motor [i = 0, 1, 2] has 3 states {off = 0, dir1 = 1, dir2 = 2}

#input keys, the ROV drives like a tank. Forwards and reverse on each side to turn
RISING = pygame.K_w
DIVING = pygame.K_s
PORT_GO = pygame.K_q
PORT_BACK = pygame.K_a
STARBOARD_GO = pygame.K_e
STARBOARD_BACK = pygame.K_d

PICTURE = pygame.K_SPACE

#function definitions
def text(content, xPos, yPos):
    #string text to display, x and y position to display the text
    font = pygame.font.Font(None, 25)
    text = font.render(str(content), 1, (255, 255, 255))
    screen.blit(text, (xPos, yPos))

