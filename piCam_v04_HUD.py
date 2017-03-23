import sys, pygame, pygame.camera, os, time
# to add the piCam to the list of available cameras, run command:
# sudo modprobe bcm2835-v4l2

os.system("sudo modprobe bcm2835-v4l2")
pygame.init()
pygame.camera.init()
FPS = 60
fpsClock = pygame.time.Clock()
imgCounter = 0

#Image sizes
picWidth = 600
picHeight = int((picWidth*9)/16)

color1 = (128, 0, 128)
color2 = (0, 0, 0)
#screen = pygame.display.set_mode((900, 600), 0)
screen = pygame.display.set_mode((800,450), pygame.FULLSCREEN)
cam_list = pygame.camera.list_cameras()
cam = pygame.camera.Camera(cam_list[0], (picWidth,picHeight))
cam.start()

def texts(h, w):
   font=pygame.font.Font(None,15)
   scoretext=font.render(str(w) + " : " + str(h), 1,(255,255,255))
   screen.blit(scoretext, (20, 20))

while True:
	image1 = cam.get_image()
	image1 = pygame.transform.scale(image1, (900, 600))
	#screen.blit(image1, (190, 60))
	screen.blit(image1, (0, 0))
	texts(picHeight, picWidth)
	pygame.display.update()
	fpsClock.tick(FPS)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
			cam.stop()
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYUP and event.key == pygame.K_UP:
			cam.stop()
			cam = pygame.camera.Camera(cam_list[0], (1024,768))
			cam.start()
			img = cam.get_image()
			pygame.image.save(img, "pic_%s.jpg" %imgCounter)
			imgCounter = imgCounter + 1
			cam.stop()
			cam = pygame.camera.Camera(cam_list[0], (picWidth, picHeight))
			cam.start()
		if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
			screen.fill(color2)
		if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
			picWidth -= 100
			picHeight = int((picWidth*9)/16)
			cam.stop()
			cam = pygame.camera.Camera(cam_list[0], (picWidth, picHeight))
			cam.start()
		if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
			picWidth += 100
			picHeight = int((picWidth*9)/16)
			cam.stop()
			cam = pygame.camera.Camera(cam_list[0], (picWidth, picHeight))
			cam.start()
