import pygame
import random

class TreeObstacle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.name = "tree"
        self.width = 40
        self.height = 360
        self.rect = pygame.Rect((self.x-30, self.y), (self.width, self.height))
        self.img1 = pygame.image.load("gameart/gameart/png&gif/gameplay/rocks/ground/rock1.png")
        self.img2 = pygame.image.load("gameart/gameart/png&gif/gameplay/rocks/ground/rock2.png")
        self.img3 = pygame.image.load("gameart/gameart/png&gif/gameplay/rocks/ground/rock3.png")
        self.img4 = pygame.image.load("gameart/gameart/png&gif/gameplay/rocks/ground/rock4.png")
        self.img5 = pygame.image.load("gameart/gameart/png&gif/gameplay/rocks/ground/rock5.png")
        img1 = pygame.transform.scale(self.img1, (108, 360)).convert_alpha()
        img2 = pygame.transform.scale(self.img2, (108, 360)).convert_alpha()
        img3 = pygame.transform.scale(self.img3, (108, 360)).convert_alpha()
        img4 = pygame.transform.scale(self.img4, (108, 360)).convert_alpha()
        img5 = pygame.transform.scale(self.img5, (108, 360)).convert_alpha()

        self.img_list = [img1, img2, img3, img4, img5]

        self.img = self.img_list[random.randint(0, 4)]



    def move(self, speed):
        self.x += speed
        self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))