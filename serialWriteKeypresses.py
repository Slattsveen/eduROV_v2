import serial, time, pygame

pygame.init()
screen = pygame.display.set_mode((600, 400), 0)

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=0.05)
ser.close()
ser.open()

#keyname definitions
RISING = pygame.K_w
DIVING = pygame.K_s
PORT_GO = pygame.K_q
PORT_BACK = pygame.K_a
STARBOARD_GO = pygame.K_e
STARBOARD_BACK = pygame.K_d

PICTURE = pygame.K_SPACE

states = [0, 0, 0]
state = "000"
lastState = "000"

def printState(array):
        msg = ""
        for val in array:
                msg += str(val)
        print(msg)
        return(msg)

while True:

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        ser.close()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                        states[1] = 1
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                        states[1] = 2
                if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                        states[0] = 1
                if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                        states[0] = 2
                if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                        states[2] = 2
                if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                        states[2] = 1
                if event.type == pygame.KEYUP and event.key == pygame.K_a:
                        states[1] = 0
                if event.type == pygame.KEYUP and event.key == pygame.K_q:
                        states[1] = 0
                if event.type == pygame.KEYUP and event.key == pygame.K_w:
                        states[0] = 0
                if event.type == pygame.KEYUP and event.key == pygame.K_s:
                        states[0] = 0
                if event.type == pygame.KEYUP and event.key == pygame.K_e:
                        states[2] = 0
                if event.type == pygame.KEYUP and event.key == pygame.K_d:
                        states[2] = 0
        state = printState(states)

        if state != lastState:
                lastState = state
                #try:
                ser.write(state)
#time.sleep(2)
                print("Sent commands")
                #except:
                 #       pass
        time.sleep(0.5)
