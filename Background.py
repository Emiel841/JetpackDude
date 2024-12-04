import pygame

class BackgroundHandler():

    def __init__(self, s_width, s_height):
        self.layer1 = pygame.image.load("gameart/gameart/png&gif/background/layer1.png")
        self.layer2 = pygame.image.load("gameart/gameart/png&gif/background/layer2.png")
        self.layer3 = pygame.image.load("gameart/gameart/png&gif/background/layer3(lights,transparent).png")
        self.layer4 = pygame.image.load("gameart/gameart/png&gif/background/layer4.png")
        self.layer5 = pygame.image.load("gameart/gameart/png&gif/background/layer5.png")
        self.layer6 = pygame.image.load("gameart/gameart/png&gif/background/layer6.png")

        self.layer1 = pygame.transform.scale(self.layer1, (s_width, s_height)).convert_alpha()
        self.layer2 = pygame.transform.scale(self.layer2, (s_width, s_height)).convert_alpha()
        self.layer3 = pygame.transform.scale(self.layer3, (s_width, s_height)).convert_alpha()
        self.layer4 = pygame.transform.scale(self.layer4, (s_width, s_height)).convert_alpha()
        self.layer5 = pygame.transform.scale(self.layer5, (s_width, s_height)).convert_alpha()
        self.layer6 = pygame.transform.scale(self.layer6, (s_width, s_height)).convert_alpha()

        self.img = pygame.image.load("gameart/gameart/png&gif/background/bacground.png")
        self.img = pygame.transform.scale(self.img, (s_width, s_height)).convert_alpha()

        self.locations = [0, 1280, 2560]

    def move(self, speed):
        for location in self.locations:
            self.locations[self.locations.index(location)] -= speed