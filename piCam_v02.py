import sys, pygame, pygame.camera, os, time
# to add the piCam to the list of available cameras, run command:
# sudo modprobe bcm2835-v4l2

os.system("sudo modprobe bcm2835-v4l2")
pygame.init()
pygame.camera.init()
FPS = 60
fpsClock = pygame.time.Clock()

color1 = (128, 0, 128)
color2 = (0, 0, 0)
#screen = pygame.display.set_mode((900, 600), 0)
screen = pygame.display.set_mode((900,600), pygame.FULLSCREEN)
cam_list = pygame.camera.list_cameras()
cam = pygame.camera.Camera(cam_list[0], (400,320))
cam.start()

while True:
	image1 = cam.get_image()
	image1 = pygame.transform.scale(image1, (900, 600))
	#screen.blit(image1, (190, 60))
	screen.blit(image1, (0, 0))
	pygame.display.update()
	fpsClock.tick(FPS)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
			cam.stop()
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYUP and event.key == pygame.K_UP:
			os.system("raspivid -o test -t 10000 -n")
		if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
			screen.fill(color2)
