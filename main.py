import config, pygame, random
from Enemy import Enemy
from Player import Player
from config import collide, window, background, laser, ship, font

# Cấu hình
WIDTH, HEIGHT, WIN = window()
RED_SPACE_SHIP, GREEN_SPACE_SHIP, BLUE_SPACE_SHIP, YELLOW_SPACE_SHIP = ship()
RED_LASER, GREEN_LASER, BLUE_LASER, YELLOW_LASER = laser()
BG = background(WIDTH, HEIGHT)
main_font, lost_font, _ = font()
enemy_vel = config.enemy_vel
laser_vel = config.laser_vel
player_vel = config.player_vel

# Hàm xử lí chính
def main():
    run = True
    lost = False
    level = config.level
    lives = config.lives
    wave_length = config.wave_length
    FPS = config.FPS
    lost_count = 0
    enemies = []
    player = Player(300, 630)
    clock = pygame.time.Clock()

    def redraw_window():
        # Thiết lập background tại vị trí (0,0)
        WIN.blit(BG, (0,0))
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))
        WIN.blit(lives_label, (10,10))
        WIN.blit(level_label, (WIDTH-level_label.get_width()-10, 10))

        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)  # Hiển thị tàu của người chơi
        if lost:
            lost_label = lost_font.render("GAME OVER!", 1, (255, 255, 255))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))

        pygame.display.update()

    # Vòng lặp vô hạn xử lí chương trình
    while run:
        clock.tick(FPS) # Thiết lập mức FPS
        redraw_window()
        if player.health <= 0:
            player.health = 100
            lives -= 1

        if lives <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                # Khởi tạo ngẫu nhiên tàu địch, có thể thêm ý tưởng: tàu đỏ nhiều máu hơn tàu xanh, ...
                enemy = Enemy(random.randrange(50, WIDTH-100),
                              random.randrange(-1500, -100), random.choice(['red', 'green', 'blue']))
                enemies.append(enemy)

        # Kiểm tra sự kiện
        for event in pygame.event.get():
            # Bắt sự kiện nếu người dùng ấn thoát game
            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0: # left
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width()< WIDTH: # right
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0: # up
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() + 15 < HEIGHT: # down (cộng thêm 15 pixel của thanh máu)
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_laser(laser_vel, player)
            # Tạo xác suất bắn của kẻ địch (random giá trị nếu = 1 thì mới bắn, 3*FPS => 1/3)
            if random.randrange(0, 3*FPS) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)

            # Nếu tàu địch đã đi khỏi màn hình thì một mạng sẽ bị trừ đi, đồng thời xóa tàu địch khỏi list enemies
            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        player.move_laser(-laser_vel, enemies)