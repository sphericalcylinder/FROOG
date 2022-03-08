import random, pygame
from street import Street
from river import River

class Generator:

    def __init__(self):
        self.streets = []
        self.rivers = []

    def generate(self):
        height = 400
        num = 2
        flipflop = False
        for i in range(7):
            if flipflop:
                flipflop = False
                direction = 'Left'
            else:
                flipflop = True
                direction = 'Right'
            rand = random.randint(0, 4)
            match rand:
                case 0:
                    self.streets.append(Street(height, direction, random.randint(1, 3)))
                    height -= 40
                    num = 0
                case 1:
                    self.streets.append(Street(height, direction, random.randint(1, 3)))
                    height -= 40
                    num = 0
                case 2:
                    if num == 0 or num == 1:
                        height += 10
                    self.rivers.append(River(height, direction, random.randint(1, 3)))
                    height -= 30
                    num = 1
                case 3:
                    if num == 0 or num == 1:
                        height += 10
                    self.rivers.append(River(height, direction, random.randint(1, 3)))
                    height -= 30
                    num = 1
                case 4:
                    height -= 40
        