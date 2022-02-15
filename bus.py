import pygame

class Bus(pygame.sprite.Sprite):

    STARTING_POSITION = (300, 250)
    SIZE = (60, 30)
    SCREEN_DIM = 600, 500
    MOVE_DIST = 2
    LEFT_IMAGE = pygame.image.load('phostos/bus_left.png')
    RIGHT_IMAGE = pygame.image.load('phostos/bus_right.png')

    def __init__(self, starting_position: tuple, direction: str):
        super().__init__()
        self.image = Bus.LEFT_IMAGE if direction == 'Left' else Bus.RIGHT_IMAGE
        self.rect = pygame.Rect((0, 0), Bus.SIZE)
        self.rect.center = Bus.STARTING_POSITION
        self.direction = direction

    def move(self):
        if self.direction == 'Left':
            self.rect.centerx -= Bus.MOVE_DIST
            if self.rect.right <= 0:
                self.rect.centerx = Bus.SCREEN_DIM[0] + Bus.SIZE / 2
        else:
            self.rect.centerx += Bus.MOVE_DIST
            if self.rect.left >= Bus.SCREEN_DIM[0]:
                self.rect.centerx = -Bus.SIZE / 2