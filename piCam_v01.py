import sys, pygame, pygame.camera

pygame.init()
pygame.camera.init()

screen = pygame.display.set_mode((1280, 720), 0)
cam_list = pygame.camera.list_cameras()
cam = pygame.camera.Camera(cam_list[0], (900,600))
cam.start()

while True:
	image1 = cam.get_image()
#	image1 = pygame.transform.scale(image1, (1280, 720))
	screen.blit(image1, (190, 60))
	pygame.display.update()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			cam.stop()
			pygame.quit()
			sys.exit()
