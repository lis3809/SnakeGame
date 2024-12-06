import pygame
import random

# Инициализация Pygame
pygame.init()

# Размер окна
WIDTH, HEIGHT = 800, 600

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Создание окна
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")

# Скорость змейки
speed = 5

# Задание начального положения змейки
snake = [(200, 200), (210, 200), (220, 200), (230, 200)]
direction = 'RIGHT'

# Задание начального положения фрукта
fruit = (random.randint(0, WIDTH - 10), random.randint(0, HEIGHT - 10))


# Функция отрисовки змейки и фрукта
def draw_snake():
    for segment in snake:
        pygame.draw.rect(window, GREEN, (segment[0], segment[1], 10, 10))
    pygame.draw.rect(window, RED, (fruit[0], fruit[1], 10, 10))


# Функция проверки столкновения змейки с границами поля или с собой
def check_collision():
    if snake[0][0] < 0 or snake[0][0] >= WIDTH or snake[0][1] < 0 or snake[0][1] >= HEIGHT:
        return True
    if snake[0] in snake[1:]:
        return True
    return False

# Функция проверки столкновений с яблоком
def is_collided_with_apple(rect_1, rect_2):
    return rect_1.colliderect(rect_2)


# Основной игровой цикл
clock = pygame.time.Clock()
running = True
while running:
    window.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            if event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            if event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'

    # Движение змейки
    if direction == 'UP':
        new_head = (snake[0][0], snake[0][1] - 10)
    if direction == 'DOWN':
        new_head = (snake[0][0], snake[0][1] + 10)
    if direction == 'LEFT':
        new_head = (snake[0][0] - 10, snake[0][1])
    if direction == 'RIGHT':
        new_head = (snake[0][0] + 10, snake[0][1])

    snake = [new_head] + snake[:-1]

    # Проверка столкновения
    if check_collision():
        print("collision")
        # running = False


    # Проверка поедания фрукта
    rect_11 = pygame.Rect(snake[0], (10, 10))
    rect_22 = pygame.Rect(fruit, (10, 10))
    if is_collided_with_apple(rect_11, rect_22):
        snake.append((0, 0))  # добавляем новую "голову" змейке
        fruit = (random.randint(0, WIDTH - 10), random.randint(0, HEIGHT - 10))




    # Отрисовка змейки и фрукта
    draw_snake()

    pygame.display.update()
    clock.tick(speed)
