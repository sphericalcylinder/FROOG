import pygame, sys, random
from froog import Froog
#Froog pronounced "Froog"
from bus import Bus
from street import Street
from log import Log

pygame.init()

SCREEN_DIM = WIDTH, HEIGHT = 600, 500
SCREEN = pygame.display.set_mode(SCREEN_DIM)
pygame.display.set_caption("Froog go spEEd")
pygame.event.set_allowed([pygame.KEYDOWN, pygame.QUIT])

CLOCK = pygame.time.Clock()
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (28, 128, 28)
YELLOW = (100, 85, 0)
BROWN = (118, 92, 72)
GRAY = (175, 175, 175)
BLUE = (0, 0, 175)

froog = Froog()
log = Log(Log.STARTING_POSITION, 'Left')

streets = []
number_of_buses = 3
street_height = 400

for _ in range(2):
	streets.append(Street(street_height, 'Left',
random.randint(1, number_of_buses)))
	streets.append(Street(street_height - 40, 'Right',
random.randint(1, number_of_buses)))
	street_height -= 80

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


	for street in streets:
		SCREEN.fill(GRAY, street.rect)
		for bus in street.buses:
			SCREEN.blit(bus.image, bus.rect)
			bus.move()
			if froog.rect.colliderect(bus.rect):
				froog.reset_position()


	if froog.rect.colliderect(log.rect):
		froog.move_on_log(log)

	bus.move()
	log.move()
	
	SCREEN.blit(log.image, log.rect)
	SCREEN.blit(froog.image, froog.rect)


	pygame.display.flip()