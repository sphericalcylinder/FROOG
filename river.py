import pygame, random
from loog import Loog


class River:

    SIZE = (600, 30)
    SCREEN_DIM = 600, 500

    def __init__(self, river_height: int, direction: str,
        number_of_loogs: int):
        self.rect = pygame.Rect((0, river_height), River.SIZE)
        self.loogs = []
        self.add_loogs(direction, number_of_loogs, river_height + 15)


    def add_loogs(self, direction: str, number_of_loogs: int, river_height: int): 
        dp = []
        for _ in range(number_of_loogs):
            while True:
                x_pos = random.randint(30, 570)
                valid = True
                for i in range(x_pos - 60, x_pos + 60):
                    if i in dp:
                        valid = False
                if valid:
                    dp.append(x_pos)
                    break
            self.loogs.append(Loog((x_pos, river_height), direction))
