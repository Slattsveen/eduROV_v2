import sys, pygame, pygame.camera, os, time, serial
from sense_hat import SenseHat
# to add the piCam to the list of available cameras, run command:
# sudo modprobe bcm2835-v4l2
os.system("sudo modprobe bcm2835-v4l2")

##ititiating pygame module, camera, serial port, senseHat
pygame.init()
pygame.camera.init()
senseHat = SenseHat()
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0.050) 
ser.close()
ser.open()
FPS = 35 #image updating frequenzy
fpsClock = pygame.time.Clock()
imgCounter = 0 #counter variable for numbering still frames taken during mission

width, height = 900, 600
picWidth, picHeight = 600, 400

##sensor variables, internally and externally of the ROV hull
tempROV = senseHat.get_temperature()
pressureROV = senseHat.get_pressure()
bearingROV = senseHat.get_compass() #gives compas bearing in degrees from North
humidityROV = senseHat.get_humidity()
orientationROV = senseHat.get_orientation() #a dict containgin values with tags 'pitch', 'roll', 'yaw'
batteryVoltage = 0
tempWater = 0
pressureWater = 0

motorStates = "000" #each motor [i = 0, 1, 2] has 3 states {off = 0, dir1 = 1, dir2 = 2}

##input keys, the ROV drives like a tank. Forwards and reverse on each side to turn
RISING = pygame.K_w
DIVING = pygame.K_s
PORT_GO = pygame.K_q
PORT_BACK = pygame.K_a
STARBOARD_GO = pygame.K_e
STARBOARD_BACK = pygame.K_d

PICTURE = pygame.K_SPACE

##color definitions
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

##import GUI elements (sprites), setup main screen
screen = pygame.display.set_mode((900, 600), 0)
#screen = pygame.display.set_mode((900, 600), pygame.FULLSCREEN)

##camera feed setup
cam_list = pygame.camera.list_cameras()
cam = pygame.camera.Camera(cam_list[0], (picWidth, picHeight))
cam.start()

##function definitions
def text(content, xPos, yPos):
    #string text to display, x and y position of the text to be displayed
    font = pygame.font.Font(None, 25)
    text = font.render(str(content), 1, (255, 255, 255))
    screen.blit(text, (xPos, yPos))


#main while loop
while True:
    ##update camera feed with a new image
    streamImage = cam.get_image()
    streamImage = pygame.transform.scale(streamImage, (900, 600))
    screen.blit(streamImage, (0, 0)) #the camera feed now covers the whole window

    ##read sensor data
    #receive serial message with sensor data from Arduino
    serialInput = " "
    #if ser.inWaiting():
    #    serialInput = ser.readline()
    #    #print(serialInput)
    #if serialInput.count(':') == 2: #check that the message is complete
    #    tempWater, pressureWater, batteryVoltage = serialInput.split(':')

    #update sensor values from the onboard senseHat
    tempROV = senseHat.get_temperature()
    pressureROV = senseHat.get_pressure()
    bearingROV = senseHat.get_compass()
    humidityROV = senseHat.get_humidity()
    orientationROV = senseHat.get_orientation()

    #write sensorvalues to screen
    text((str(batteryVoltage) + "V"), 750, 20)
    text("Outside ROV:", 20, 120)
    text((str(tempWater) + " C"), 20, 145)
    text(str(pressureWater), 20, 170)

    text("Inside ROV:", 750, 120)
    text((str(tempWater) + " C"), 750, 145)
    text(str(pressureROV), 750, 170)

    ##read keyboard input
    serialOutput = "0" #dive/rise, portRev/fortFwd, strbdRev/strbdFwd
    #buttonflags = 
    for event in pygame.event.get():
        #user closes the streaming window
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            cam.stop()
            ser.close()
            pygame.quit()
            sys.exit()

        #user presses a key
        if event.type == pygame.KEYDOWN and event.key == DIVING:
            serialOutput = "1"
        elif event.type == pygame.KEYDOWN and event.key == RISING:
            serialOutput = "2"
        if event.type == pygame.KEYUP and (event.key == DIVING or event.key == RISING):
            serialOutput = "0"
        #else:
        #    serialOutput = "0"
        if event.type == pygame.KEYDOWN and event.key == PORT_BACK:
            serialOutput += "1"
        elif event.type == pygame.KEYDOWN and event.key == PORT_GO:
            serialOutput += "2"
        if event.type == pygame.KEYUP and (event.key == PORT_BACK or event.key == PORT_GO):
            serialOutput += "0"
        #else:
        #    serialOutput += "0"
        if event.type == pygame.KEYDOWN and event.key == STARBOARD_BACK:
            serialOutput += "1"
        elif event.type == pygame.KEYDOWN and event.key == STARBOARD_GO:
            serialOutput += "2"
        if event.type == pygame.KEYUP and (event.key == STARBOARD_BACK or event.key == STARBOARD_GO):
            serialOutput += "0"
        #else:
        #    serialOutput += "0"
        print(serialOutput)
    ##update the whole screen image
    pygame.display.flip()
    fpsClock.tick(FPS)

    
