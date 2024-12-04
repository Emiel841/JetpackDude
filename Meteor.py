import random
import pygame


class MeteorObstacle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.name = "meteor"
        self.width = 90
        self.height = 90
        self.rect = pygame.Rect((self.x, self.y), (self.width-30, self.height-15))
        img1 = pygame.image.load("gameart/gameart/png&gif/gameplay/rocks/falling1.png")
        img2 = pygame.image.load("gameart/gameart/png&gif/gameplay/rocks/falling2.png")
        img3 = pygame.image.load("gameart/gameart/png&gif/gameplay/rocks/falling3.png")
        img4 = pygame.image.load("gameart/gameart/png&gif/gameplay/rocks/falling4.png")
        img5 = pygame.image.load("gameart/gameart/png&gif/gameplay/rocks/falling5.png")
        img6 = pygame.image.load("gameart/gameart/png&gif/gameplay/rocks/falling6.png")

        img1 = pygame.transform.scale(img1, (self.width, self.height)).convert_alpha()
        img2 = pygame.transform.scale(img2, (self.width, self.height)).convert_alpha()
        img3 = pygame.transform.scale(img3, (self.width, self.height)).convert_alpha()
        img4 = pygame.transform.scale(img4, (self.width, self.height)).convert_alpha()
        img5 = pygame.transform.scale(img5, (self.width, self.height)).convert_alpha()
        img6 = pygame.transform.scale(img6, (self.width, self.height)).convert_alpha()

        self.img_list = [img1, img2, img3, img4, img5, img6]

        self.img = self.img_list[random.randint(0, 5)]



    def move(self, speed):
        self.x += speed*3
        self.y -= (speed + 1)
        self.rect = pygame.Rect((self.x, self.y), (self.width-30, self.height-15))