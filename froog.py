import pygame
from loog import Loog

class Froog(pygame.sprite.Sprite):

	STARTING_POSITION = (300, 490)
	SIZE = (20, 10)
	IMAGE = pygame.image.load('phostos/froog.png')
	MOVE_DIST = 10
	SCREEN_DIM = 600, 500

	def __init__(self, hacks: bool):
		super().__init__()
		self.image = Froog.IMAGE
		self.rect = pygame.Rect((0, 0), Froog.SIZE)
		self.rect.center = Froog.STARTING_POSITION
		self.lives = 3
		self.hacks = hacks

	def move_up(self):
		if self.rect.top >= 20:
			self.rect.centery -= Froog.MOVE_DIST

	def move_down(self):
		if self.rect.bottom <= Froog.SCREEN_DIM[1] - 20:
			self.rect.centery += Froog.MOVE_DIST

	def move_left(self):
		if self.rect.left >= 20:
			self.rect.centerx -= Froog.MOVE_DIST

	def move_right(self):
		if self.rect.right <= Froog.SCREEN_DIM[0] - 20:
			self.rect.centerx += Froog.MOVE_DIST

	def reset_position(self):
		self.rect.center = Froog.STARTING_POSITION
		self.lives -= 1

	def move_on_loog(self, loog: Loog):
		if loog.direction == 'Left':
			self.rect.centerx -= Loog.MOVE_DIST
			if self.rect.right <= 0:
				if self.hacks:
					self.rect.centerx = Loog.SCREEN_DIM[0] + Loog.SIZE[0] / 2
				else:
					self.reset_position()
				
		else:
			self.rect.centerx += Loog.MOVE_DIST
			if self.rect.left >= loog.SCREEN_DIM[0]:
				if self.hacks:
					self.rect.centerx = -Loog.SIZE[0] / 2
				else:
					self.reset_position()