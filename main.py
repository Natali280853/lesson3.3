import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGTH = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HIGTH))
pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/девушка с пистолетом1.png")
pygame.display.set_icon(icon)

target_image = pygame.image.load("img/чизбургер.png")
target_width =80
target_heigth =80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGTH - target_heigth)

color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))


running = True
while running:
    pass

pygame.quit()