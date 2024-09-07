import pygame
import random

# инициализация Pygame
pygame.init()

# определение игрового поля
WIDTH, HEIGTH = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGTH))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/девушка с пистолетом1.png")
pygame.display.set_icon(icon)

# начальные координаты цели
target_img = pygame.image.load("img/чизбургер.png")
target_width, target_heigth = 80, 80
target_x = random.randint(0, WIDTH - target_width)
target_y = random.randint(0, HEIGTH - target_heigth)
target_radius = 80
speed_x = random.choice([-1, 1]) * random.randint(1, 3)
speed_y = random.choice([-1, 1]) * random.randint(1, 3)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# инициализация
mouse_x, mouse_y = WIDTH // 2, HEIGTH - 20
bullet_fired = False

# основной игровой цикл
running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if not bullet_fired:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                bullet_fired = True

    # обновление координат цели
    target_x += speed_x
    target_y += speed_y
    if target_x + target_radius > WIDTH or target_x < 0:
        speed_x = -speed_x
    if target_y + target_radius > HEIGTH or target_y < 0:
        speed_y = -speed_y

    # проверка попадания в цель
    if bullet_fired and abs(mouse_x - target_x) <= target_radius and abs(mouse_y - target_y) <= target_radius:
        target_x = random.randint(0, WIDTH - target_width)
        target_y = random.randint(0, HEIGTH - target_heigth)
        speed_x = random.choice([-1, 1]) * random.randint(1, 3)
        speed_y = random.choice([-1, 1]) * random.randint(1, 3)
        bullet_fired = False

    # очистка экрана
    screen.fill(color)

    # рисуем цель
    screen.blit(target_img, (target_x, target_y))

    # Обновление экрана
    pygame.display.update()

    # обновляем экран
    pygame.display.flip()

    # устанавливаем частоту обновления экрана
    pygame.time.Clock().tick(60)

# завершение работы Pygame
pygame.quit()
