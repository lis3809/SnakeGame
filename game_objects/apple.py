import pygame as pg
import random


def load_img(name):
    img = pg.image.load(name)
    img = img.convert()
    colorkey = img.get_at((0, 0))
    img.set_colorkey(colorkey)
    img = pg.transform.scale(img, (30, 30))
    return img

class Apple(pg.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        pg.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = load_img("picture/apple.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,  screen.get_width() - self.rect.width)
        self.rect.y = random.randint(0,  screen.get_height() - self.rect.height)

    # def update(self):
        # self.rect.x = random.randint(0,  self.screen.get_width() - self.rect.width)
        # self.rect.y = random.randint(0,  self.screen.get_height() - self.rect.height)

    def draw(self):
        self.screen.blit(self.image, self.rect)
