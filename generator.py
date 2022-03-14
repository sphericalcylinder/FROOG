import random
from street import Street
from river import River

class Generator:

    def __init__(self):
        self.streets = []
        self.rivers = []
        self.num_cars = 3
        self.num_loogs = 3

    def generate_random(self):
        height = 400
        flipflop = False
        rand = -1
        notriver = False
        for i in range(10):
            if i == 5:
                height -= 40
            if flipflop:
                flipflop = False
                direction = 'Left'
            else:
                flipflop = True
                direction = 'Right'
            rand = random.randint(0, 1)
            match rand:
                case 0:
                    self.streets.append(Street(height, direction, random.randint(1, self.num_cars)))
                    height -= 40
                    notriver = True
                case 1:
                    if notriver:
                        height += 10
                    self.rivers.append(River(height, direction, random.randint(1, self.num_loogs)))
                    height -= 30
                    notriver = False

               
    def generate_uniform(self):
        street_height = 400
        river_height = 200

        for e in range(2):
            self.streets.append(Street(street_height, 'Left',
                random.randint(1, self.num_cars)))
            self.streets.append(Street(street_height - 40, 'Right',
                random.randint(1, self.num_cars)))
            street_height -= 80

        for e in range(2):
            self.rivers.append(River(river_height, 'Left',
                random.randint(1, self.num_loogs)))
            self.rivers.append(River(river_height - 30, 'Right',
                random.randint(1, self.num_loogs)))
            river_height -= 60


    def generate_impossible(self):
            self.rivers.append(River(200, 'Right', 0))