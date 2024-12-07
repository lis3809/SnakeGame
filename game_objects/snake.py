# Класс объекта игрока
import pygame as pg
import game_config


def load_img(name):
    img = pg.image.load(name)
    # img = img.convert()
    # colorkey = img.get_at((0, 0))
    # img.set_colorkey(colorkey)
    img = pg.transform.scale(img, (game_config.size_segment_snake, game_config.size_segment_snake))
    return img


class Snake():
    def __init__(self, screen):
        self.screen = screen
        self.bodySprites = pg.sprite.Group()

        self.listBodySnake = []
        for i in range(3):
            body = SnakeSegment(screen,
                                game_config.WINDOW_SIZE[0] // 2 + game_config.size_segment_snake * i,
                                game_config.WINDOW_SIZE[1] // 2)
            self.listBodySnake.append(body)

        self.direction = 'RIGHT'
        self.speed = game_config.size_segment_snake

    def update(self):
        keys = pg.key.get_pressed()

        #Определяем направление движения
        if keys[pg.K_UP] and self.direction != 'DOWN':
            self.direction = 'UP'
        if keys[pg.K_DOWN] and self.direction != 'UP':
            self.direction = 'DOWN'
        if keys[pg.K_LEFT] and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if keys[pg.K_RIGHT] and self.direction != 'LEFT':
            self.direction = 'RIGHT'

        # Двигаем змейку
        old_head = self.listBodySnake[0]
        if self.direction == 'UP':
            new_head = SnakeSegment(self.screen, old_head.rect.x, old_head.rect.y - self.speed)
        if self.direction == 'DOWN':
            new_head = SnakeSegment(self.screen, old_head.rect.x, old_head.rect.y + self.speed)
        if self.direction == 'LEFT':
            new_head = SnakeSegment(self.screen, old_head.rect.x - self.speed, old_head.rect.y)

        if self.direction == 'RIGHT':
            new_head = SnakeSegment(self.screen, old_head.rect.x + self.speed, old_head.rect.y)

        self.listBodySnake.insert(0, new_head)  # Добавляем новую голову
        self.listBodySnake.pop()  # Удаляем последний элемент

    def draw(self):
        for snakeSegment in self.listBodySnake:
            snakeSegment.draw()


class SnakeSegment(pg.sprite.Sprite):
    def __init__(self, screen, x, y):
        super().__init__()
        self.screen = screen
        self.image = load_img("picture/snake_body.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        self.screen.blit(self.image, self.rect)
