import pygame, sys
from froog import Froog
#Froog pronounced "Froog"
from generator import Generator
from river import River

pygame.init()

SCREEN_DIM = WIDTH, HEIGHT = 600, 500
SCREEN = pygame.display.set_mode(SCREEN_DIM)
pygame.display.set_caption("Froog Highway")
pygame.event.set_allowed([pygame.KEYDOWN, pygame.QUIT])
watereffect = pygame.mixer.music.load('phostos/water.mp3')

CLOCK = pygame.time.Clock()
FPS = 60
HACKS = False
RANDOM_TERRAIN = True
IMPOSSIBLE = True

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (28, 128, 28)
YELLOW = (100, 85, 0)
BROWN = (118, 92, 72)
GRAY = (175, 175, 175)
BLUE = (0, 0, 175)

froog = Froog(HACKS)

levels = []

for g in range(10):
	levels.append(Generator())


if RANDOM_TERRAIN:
	if not IMPOSSIBLE:
		for h in levels:
			h.generate_random()
	else:
		for h in levels:
			h.generate_random()
		levels[9].generate_impossible()
else:
	for h in levels:
		h.generate_uniform()

terrain = levels[0]

while True:
	frooglevel = Froog.LEVEL
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
			if event.key == pygame.K_BACKSLASH and not HACKS and not IMPOSSIBLE:
				HACKS = True
				froogpos = froog.rect.x, froog.rect.y
				pygame.display.set_mode(SCREEN_DIM)
				froog = Froog(HACKS)
				froog.rect.x, froog.rect.y = froogpos
				pygame.mixer.music.play(-1)
			if event.key == pygame.K_SLASH and HACKS and not IMPOSSIBLE:
				HACKS = False
				froogpos = froog.rect.x, froog.rect.y
				froog = Froog(HACKS)
				froog.rect.x, froog.rect.y = froogpos
				pygame.mixer.music.stop()

	if frooglevel != Froog.LEVEL:
		if frooglevel <= Froog.LEVEL:
			froogx = froog.rect.x
			terrain = levels[Froog.LEVEL]
			froog.rect.x = froogx
			froog.rect.y = 480
		elif frooglevel >= Froog.LEVEL:
			froogx = froog.rect.x
			terrain = levels[Froog.LEVEL]
			froog.rect.x = froogx
			froog.rect.y = 10
		print(froog.LEVEL + 1)
	
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