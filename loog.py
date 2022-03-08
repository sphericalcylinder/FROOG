import pygame

class Loog(pygame.sprite.Sprite):
    # Define constant values
    IMAGE = pygame.image.load('phostos/loog.png')
    STARTING_POSITION = (300, 150)
    SIZE = (60, 30)
    SCREEN_DIM = 600, 500
    MOVE_DIST = 1

    # Creates a loog object
    def __init__(self, starting_position: tuple, direction: str):
        # Sprite Information
        super().__init__()
        self.image = Loog.IMAGE
        # loog Information
        self.rect = pygame.Rect((0, 0), Loog.SIZE)
        self.rect.center = starting_position
        self.direction = direction

    def move(self):
        # loog is going left
        if self.direction == 'Left':
            self.rect.centerx -= Loog.MOVE_DIST
            # loog has moved off the screen
            if self.rect.right <= 0:
                self.rect.centerx = Loog.SCREEN_DIM[0] + Loog.SIZE[0] / 2
        # loog is going right
        else:
            self.rect.centerx += Loog.MOVE_DIST
            # loog has moved off the screen
            if self.rect.left >= Loog.SCREEN_DIM[0]:
                self.rect.centerx = -Loog.SIZE[0] / 2
