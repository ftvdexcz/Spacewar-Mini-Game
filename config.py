import pygame
import os
pygame.font.init() # init font pygame

# Các biến cần thiết trong chương trình
FPS = 60
level = 0
lives = 5
enemy_vel = 1
laser_vel = 4
player_vel = 5
wave_length = 5

# Thiết lập cửa sổ chương trình
def window():
    WIDTH = 750; HEIGHT = 750
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Spacewar Game")
    return WIDTH, HEIGHT, WIN

# Background
def background(WIDTH, HEIGHT):
    BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))
    return BG

# Thiết lập hình ảnh cho các đối tượng trong game (file assets)
# Hình ảnh tàu
def ship():
    RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
    GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
    BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
    YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))
    return RED_SPACE_SHIP, GREEN_SPACE_SHIP, BLUE_SPACE_SHIP, YELLOW_SPACE_SHIP

# Hình ảnh tia bắn
def laser():
    RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
    GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
    BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
    YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))
    return RED_LASER, GREEN_LASER, BLUE_LASER, YELLOW_LASER

# Font
def font():
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)
    title_font = pygame.font.SysFont("comicsans", 70)
    return main_font, lost_font, title_font

# Hàm kiểm tra va chạm giữa các đối tượng
def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None




