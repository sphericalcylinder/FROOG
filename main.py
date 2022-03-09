import pygame, sys, random
from froog import Froog
#Froog pronounced "Froog"
from street import Street
from river import River
from generator import Generator


pygame.init()

SCREEN_DIM = WIDTH, HEIGHT = 600, 500
SCREEN = pygame.display.set_mode(SCREEN_DIM)
pygame.display.set_caption("Froog Highway")
pygame.event.set_allowed([pygame.KEYDOWN, pygame.QUIT])

CLOCK = pygame.time.Clock()
FPS = 60
HACKS = False
RANDOM_TERRAIN = True

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (28, 128, 28)
YELLOW = (100, 85, 0)
BROWN = (118, 92, 72)
GRAY = (175, 175, 175)
BLUE = (0, 0, 175)

froog = Froog(HACKS)

terrain = Generator()

if RANDOM_TERRAIN:
	terrain.generate_midrandom()
elif RANDOM_TERRAIN == False:
	terrain.generate_uniform()
else:
	terrain.generate_fullrandom()




while True:
	CLOCK.tick(FPS)
	SCREEN.fill(BLACK)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				sys.exit()
			if event.key == pygame.K_w or event.key == pygame.K_UP:
				froog.move_up()
			if event.key == pygame.K_a or event.key == pygame.K_LEFT:
				froog.move_left()
			if event.key == pygame.K_s or event.key == pygame.K_DOWN:
				froog.move_down()
			if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
				froog.move_right()
			if event.key == pygame.K_BACKSLASH and event.key == pygame.K_ESCAPE:
				HACKS = True
				froog = Froog(HACKS)


	for street in terrain.streets:
		SCREEN.fill(GRAY, street.rect)
		for bus in street.buses:
			SCREEN.blit(bus.image, bus.rect)
			bus.move()
			if froog.rect.colliderect(bus.rect) and not HACKS:
				froog.reset_position()


	froog_on_loog = False
	for river in terrain.rivers:
		SCREEN.fill(BLUE, river.rect)
		for loog in river.loogs:
			SCREEN.blit(loog.image, loog.rect)
			loog.move()
			if froog.rect.colliderect(loog.rect):
				froog.move_on_loog(loog)
				froog_on_loog = True

		if froog.rect.colliderect(river.rect) and not froog_on_loog and not HACKS:
			froog.reset_position()


	SCREEN.blit(froog.image, froog.rect)

	pygame.display.flip()