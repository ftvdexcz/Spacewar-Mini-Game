import pygame
from config import window, background, font, MUSIC
from main import main
pygame.mixer.init()

WIDTH, HEIGHT, WIN = window()
BG = background(WIDTH, HEIGHT)
MUSIC = MUSIC

def main_menu():
    _, _, title_font = font()
    run = True
    pygame.mixer.music.load(MUSIC)
    pygame.mixer.music.play(-1)
    
    while run:
        WIN.blit(BG, (0,0))
        title_label = title_font.render("Press mouse to play game!", 1, (255,255,255))
        WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()

main_menu()

