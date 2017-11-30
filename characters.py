import pygame as pg
import main
import variables as v
import images as i

class Hero(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.x = v.herox
        self.y = v.heroy
        self.mapy = v.heromapy
        self.mapx = v.heromapx
        self.down = i.rowanFront
        self.down_1 = i.rowanfrontstep1
        self.down_2 = i.rowanfrontstep2
        self.up = i.rowanBack
        self.right = i.rowanRight
        self.left = i.rowanLeft
        self.map_rect = pg.Rect(self.mapx, self.mapy, 20, 40)

    def draw(self):
        if v.heroFace == 0 or v.heroFace == 3 and v.heroState == 'still':
            main.gameDisplay.blit(self.down, (self.x, self.y))
        elif v.heroFace == 0 or v.heroFace == 3 and v.heroState == 'moving':
            if self.y % 2 == 0:
                main.gameDisplay.blit(self.down_1, (self.x, self.y))
            elif self.y % 2 != 0:
                main.gameDisplay.blit(self.down_2, (self.x, self.y))
        if v.heroFace == 1:
            main.gameDisplay.blit(self.up, (self.x, self.y))
        if v.heroFace == 2:
            main.gameDisplay.blit(self.right, (self.x, self.y))
        if v.heroFace == 4:
            main.gameDisplay.blit(self.left, (self.x, self.y))

class PauseMenu():

    def __init__(self):
        self.height = main.display_height
        self.width = main.display_width
        self.color = main.blue

    def draw(self):
        pg.draw.rect(main.gameDisplay, self.color, (10, 10, self.width - 20, self.height - 20))

class Camera():

    def __init__(self):
        self.x = v.camerax
        self.y = v.cameray
        self.image = i.mappy
        self.rect = self.image.get_rect()


    def draw(self):
       main.gameDisplay.blit(self.image, (self.x, self.y))

class BlueRect(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pg.Surface([20, 20])
        self.image.fill(main.blue)
        self.rect = pg.Rect(self.x, self.y, 20, 20)

    def draw(self):
        pg.draw.rect(i.mappy, main.blue, (self.x, self.y, 20, 20))



