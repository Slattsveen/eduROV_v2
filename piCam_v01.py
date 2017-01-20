import sys, pygame, pygame.camera, os
# to add the piCam to the list of available cameras, run command:
# sudo modprobe bcm2835-v4l2

os.system("sudo modprobe bcm2835-v4l2")
pygame.init()
pygame.camera.init()

color1 = (128, 0, 128)
color2 = (0, 0, 0)
screen = pygame.display.set_mode((1280, 720), 0)
#screen = pygame.display.set_mode((1280,720), pygame.FULLSCREEN)
cam_list = pygame.camera.list_cameras()
cam = pygame.camera.Camera(cam_list[0], (900,600))
cam.start()

while True:
	image1 = cam.get_image()
#	image1 = pygame.transform.scale(image1, (1280, 720))
	screen.blit(image1, (190, 60))
	pygame.display.update()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
			cam.stop()
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYUP and event.key == pygame.K_UP:
			screen.fill(color1)
		if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
			screen.fill(color2)
