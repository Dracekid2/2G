import pygame
import sys
import random

# Inicializace Pygame
pygame.init()

# Nastavení rozměrů okna
screen_width = 1550
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))

# Nastavení názvu okna
pygame.display.set_caption('Pygame hra s červeným kolečkem')

# Barvy
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Parametry postavy
figure_x = 400
figure_y = 300
figure_radius = 30
speed = 1  # rychlost pohybu

# Funkce pro náhodné generování pozice červeného kolečka
def generate_red_circle():
    return pygame.Rect(
        random.randint(figure_radius, screen_width - figure_radius * 2),
        random.randint(figure_radius, screen_height - figure_radius * 2),
        figure_radius * 2, figure_radius * 2
    )

# Inicializace červeného kolečka
red_circle = generate_red_circle()

# Skóre
score = 0

# Hlavní smyčka programu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Zachytávání stisknutých kláves
    keys = pygame.key.get_pressed()

    # Pohyb pomocí kláves WSAD s kontrolou hranic okna
    if keys[pygame.K_w] and figure_y - figure_radius > 0:  # W - nahoru
        figure_y -= speed
    if keys[pygame.K_s] and figure_y + figure_radius < screen_height:  # S - dolů
        figure_y += speed
    if keys[pygame.K_a] and figure_x - figure_radius > 0:  # A - doleva
        figure_x -= speed
    if keys[pygame.K_d] and figure_x + figure_radius < screen_width:  # D - doprava
        figure_x += speed
    if keys[pygame.K_e]:
        speed = 2
    if keys[pygame.K_q]:
        speed = 1

    # Kontrola kolize mezi postavou a červeným kolečkem
    figure_rect = pygame.Rect(figure_x - figure_radius, figure_y - figure_radius, figure_radius * 2, figure_radius * 2)
    if figure_rect.colliderect(red_circle):
        score += 1
        red_circle = generate_red_circle()

    # Vykreslení pozadí
    screen.fill(white)  # Bílé pozadí

    # Vykreslení hlavní postavy (kruh)
    pygame.draw.circle(screen, green, (figure_x, figure_y), figure_radius)

    # Vykreslení červeného kolečka
    pygame.draw.circle(screen, red, red_circle.center, figure_radius)

    # Vykreslení skóre
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Skóre: {score}', True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Aktualizace obrazovky
    pygame.display.flip()

# Ukončení Pygame
pygame.quit()
sys.exit()
