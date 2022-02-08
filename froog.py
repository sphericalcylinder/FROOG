import pygame

class Froog(pygame.sprite.Sprite):

	STARTING_POSITION = (300, 490)
	SIZE = (20, 10)
	IMAGE = pygame.image.load('phostos/froog.png')

	def __init__(self):
		super().__init__()
		self.image = Froog.IMAGE
		self.rect = pygame.Rect((0, 0), Froog.SIZE)
		self.rect.center = Froog.STARTING_POSITION