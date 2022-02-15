import pygame

class Froog(pygame.sprite.Sprite):

	STARTING_POSITION = (300, 490)
	SIZE = (20, 10)
	IMAGE = pygame.image.load('phostos/froog.png')
	MOVE_DIST = 10
	SCREEN_DIM = 600, 500

	def __init__(self):
		super().__init__()
		self.image = Froog.IMAGE
		self.rect = pygame.Rect((0, 0), Froog.SIZE)
		self.rect.center = Froog.STARTING_POSITION

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
