import pygame


class Rocket():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.name = "rocket"
        self.width = 110
        self.height = 30
        self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))
        img1 = pygame.image.load("gameart/rocketframes/frame_0_delay-0.1s.gif")
        img2 = pygame.image.load("gameart/rocketframes/frame_1_delay-0.1s.gif")
        img3 = pygame.image.load("gameart/rocketframes/frame_2_delay-0.1s.gif")
        img4 = pygame.image.load("gameart/rocketframes/frame_3_delay-0.1s.gif")
        img1 = pygame.transform.scale(img1, (120, 60))
        img2 = pygame.transform.scale(img2, (120, 60))
        img3 = pygame.transform.scale(img3, (120, 60))
        img4 = pygame.transform.scale(img4, (120, 60))
        self.image_list = [img1, img2, img3, img4]
        self.img = img1
        self.count = 0
        self.frame = 0

    def move(self, speed):
        self.x += speed*5
        self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))
    def animate(self):
        self.count += 1
        if self.count == 5:
            self.count = 0
            self.frame += 1
            if self.frame == 4:
                self.frame = 0
            self.img = self.image_list[self.frame]