import pygame
from sys import exit

from pygame.surface import Surface, SurfaceType

pygame.init()
screen: Surface | SurfaceType = pygame.display.set_mode((800, 400))
pygame.display.set_caption("RunGame")
clock = pygame.time.Clock()
text_font = pygame.font.Font("font/Pixeltype.ttf", 50)
text_surface = text_font.render("Welcome to RunGame", False, (64, 64, 64))
text_rectangle = text_surface.get_rect(center=(400, 50))
sky_surface = pygame.image.load("graphics/sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()
snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom=(600, 300))
player_surface = pygame.image.load("graphics/Player/player_walk_2.png").convert_alpha()
player_rectangle = player_surface.get_rect(midbottom=(20, 300))
player_gravity: int = 0
game_active = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rectangle.collidepoint(event.pos) and player_rectangle.bottom >= 300:
                player_gravity = -20
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rectangle.bottom >= 300:
                player_gravity = -20
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, '#c0e8ec', text_rectangle)
    pygame.draw.rect(screen, '#c0e8ec', text_rectangle, 10)
    screen.blit(text_surface, text_rectangle)
    screen.blit(snail_surface, snail_rectangle)

    player_rectangle.right += 2
    snail_rectangle.left -= 2
    if snail_rectangle.left <= - 100:
        snail_rectangle.left = 800

    # player
    player_gravity += 1
    player_rectangle.centery += player_gravity
    if player_rectangle.bottom >= 300:
        player_rectangle.bottom = 300
    screen.blit(player_surface, player_rectangle)

    # collision
    if player_rectangle.colliderect(snail_rectangle):
        game_active = False
    pygame.display.update()
    clock.tick(60)
