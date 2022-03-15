from tkinter import S
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
IMPOSSIBLE = False

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (28, 128, 28)
YELLOW = (100, 85, 0)
BROWN = (118, 92, 72)
GRAY = (175, 175, 175)
BLUE = (0, 0, 175)

FONT = pygame.font.Font('phostos/joystix monospace.ttf', 20)
MENU_LARGE = pygame.font.Font('phostos/joystix monospace.ttf', 50)
MENU_MEDIUM = pygame.font.Font('phostos/joystix monospace.ttf', 25)
MENU_SMALL = pygame.font.Font('phostos/joystix monospace.ttf', 15)


START_MENU = True
END_MENU = False


froog = Froog(HACKS)

levels = []

for g in range(5):
	levels.append(Generator())


if RANDOM_TERRAIN:
	if not IMPOSSIBLE:
		for h in levels:
			h.generate_random()
	else:
		for h in levels:
			h.generate_random()
		levels[4].generate_impossible()
else:
	for h in levels:
		h.generate_uniform()

terrain = levels[0]


score = 0
current_best = 0
high_score = 0

while True:
	while START_MENU:
		CLOCK.tick(15)
		SCREEN.fill(GRAY)
		name = MENU_LARGE.render("Froog Highway", True, WHITE)
		instructions = MENU_SMALL.render("Press Space to start", True, WHITE)
		SCREEN.blit(name, (50, 130))
		SCREEN.blit(instructions, (80, 210))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					START_MENU = False

		pygame.display.update()

	while END_MENU:
		CLOCK.tick(15)
		SCREEN.fill(GRAY)
		thanks = MENU_MEDIUM.render("Thanks for playing!", True, WHITE)
		finalscore = MENU_MEDIUM.render(f"Your final score is: {score + current_best}", True, WHITE)
		instructions = MENU_MEDIUM.render("Press Space to play again", True, WHITE)
		SCREEN.blit(thanks, (85, 120))
		SCREEN.blit(finalscore, (70, 180))
		SCREEN.blit(instructions, (60, 240))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					froog.lives = 3
					score = 0
					current_best = 0
					END_MENU = False
					Froog.LEVEL = 0
					terrain = levels[Froog.LEVEL]

		pygame.display.update()

	CLOCK.tick(FPS)
	SCREEN.fill(BLACK)
	frooglevel = Froog.LEVEL

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
			froog.lives += 1
			score += 1000 + current_best
			current_best = 0
	
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

	if 475 - froog.rect.top > current_best:
		current_best = 475 - froog.rect.top
	
	if score + current_best >= high_score:
		high_score = score + current_best

#	if froog.rect.top <= 19:
#		froog.lives += 1
#		score += 1000 + current_best
#		current_best = 0

	if froog.lives == 0:
		END_MENU = True

	score_text = FONT.render(f"Score: {score + current_best}", True, WHITE)
	high_score_text = FONT.render(f"High Score: {high_score}", True, WHITE)
	lives_text = FONT.render(f"Lives: {froog.lives}", True, WHITE)

	SCREEN.blit(froog.image, froog.rect)
	SCREEN.blit(score_text, (5, 0))
	SCREEN.blit(high_score_text, (5, 20))
	SCREEN.blit(lives_text, (5, 40))

	pygame.display.flip()