from Ship import Ship
from Laser import Laser
from config import ship,laser
import pygame

RED_SPACE_SHIP, GREEN_SPACE_SHIP, BLUE_SPACE_SHIP, YELLOW_SPACE_SHIP = ship()
RED_LASER, GREEN_LASER, BLUE_LASER, YELLOW_LASER = laser()

class Enemy(Ship):
    # Class atribute (static)
    COLOR_MAP = {
        'red' : (RED_SPACE_SHIP, RED_LASER),
        'green' : (GREEN_SPACE_SHIP, GREEN_LASER),
        'blue' : (BLUE_SPACE_SHIP, BLUE_LASER)
    }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = Enemy.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img) # hitbox

    def move(self, vel):
        self.y += vel

    # Override
    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x-15, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1