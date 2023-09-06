import pygame
import random
import sys

# Размер окна
window_width = 212
window_height = 40

# Инициализация Pygame
pygame.init()

# Создание окна
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Starry Sky")

# Определение цветов
black = (0, 0, 0)

# Главный цикл программы
running = True
clock = pygame.time.Clock()

stars = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Очистка экрана
    screen.fill(black)

    # Создание и обновление звезд
    if random.random() < 0.2:  # Вероятность появления новой звезды
        stars.append((0, random.randint(0, window_height - 1), random.randint(50, 255)))

    new_stars = []
    for star in stars:
        x, y, brightness = star
        if x < window_width:
            pygame.draw.rect(screen, (brightness, brightness, brightness), (x, y, 1, 1))
            new_stars.append((x + 1, y, brightness))
        else:
            continue

    stars = new_stars

    pygame.display.flip()
    clock.tick(30)  # Ограничение кадров в секунду

# Завершение Pygame
pygame.quit()
sys.exit()
