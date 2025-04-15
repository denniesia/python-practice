from typing import Tuple, List
class Alien:
    health = 3
    total_aliens_created = 0
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.total_aliens_created += 1

    def is_alive(self):
        if self.health > 0:
            return True

        return False

    def hit(self):
        self.health -= 1

    def teleport(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y

    def collision_detection(self, other_object):
        pass

def new_aliens_collection(positions: List[Tuple]): #[(7,7), (-1,0)]
        aliens = []
        for pair in positions:
            aliens.append(Alien(*pair))
        return aliens




