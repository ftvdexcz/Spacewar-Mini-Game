from Ship import Ship
import pygame
from config import ship, laser, window

_,_,_,YELLOW_SPACE_SHIP = ship()
_,_,_,YELLOW_LASER = laser()
WIDTH,HEIGHT,_= window()

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img) # hitbox
        self.max_health = health

    # Override
    def move_laser(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                # Kiểm tra xem tàu địch có tàu nào va chạm với cú bắn không
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.ship_img.get_height() + 10,
                                             self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y + self.ship_img.get_height() + 10,
                                            self.ship_img.get_width() * (self.health/self.max_health), 10))