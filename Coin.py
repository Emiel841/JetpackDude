import pygame


class Coin():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radious = 20
        self.rect = ((x-10, y-10), (20, 20))
        self.name = "coin"
        width = 40
        height = 40
        img1 = pygame.image.load("gameart/coinframes/frame_00_delay-0.1s.gif")
        img2 = pygame.image.load("gameart/coinframes/frame_01_delay-0.1s.gif")
        img3 = pygame.image.load("gameart/coinframes/frame_02_delay-0.1s.gif")
        img4 = pygame.image.load("gameart/coinframes/frame_03_delay-0.1s.gif")
        img5 = pygame.image.load("gameart/coinframes/frame_04_delay-0.1s.gif")
        img6 = pygame.image.load("gameart/coinframes/frame_05_delay-0.1s.gif")
        img7 = pygame.image.load("gameart/coinframes/frame_06_delay-0.1s.gif")
        img8 = pygame.image.load("gameart/coinframes/frame_07_delay-0.1s.gif")
        img9 = pygame.image.load("gameart/coinframes/frame_08_delay-0.1s.gif")
        img10 = pygame.image.load("gameart/coinframes/frame_09_delay-0.1s.gif")
        img11 = pygame.image.load("gameart/coinframes/frame_10_delay-0.1s.gif")
        img12 = pygame.image.load("gameart/coinframes/frame_11_delay-0.1s.gif")
        img13 = pygame.image.load("gameart/coinframes/frame_12_delay-0.1s.gif")
        img14 = pygame.image.load("gameart/coinframes/frame_13_delay-0.1s.gif")
        img15 = pygame.image.load("gameart/coinframes/frame_14_delay-0.1s.gif")
        img16 = pygame.image.load("gameart/coinframes/frame_15_delay-0.1s.gif")
        img17 = pygame.image.load("gameart/coinframes/frame_16_delay-0.1s.gif")
        img18 = pygame.image.load("gameart/coinframes/frame_17_delay-0.1s.gif")
        img19 = pygame.image.load("gameart/coinframes/frame_18_delay-0.1s.gif")
        img20 = pygame.image.load("gameart/coinframes/frame_19_delay-0.1s.gif")
        img21 = pygame.image.load("gameart/coinframes/frame_20_delay-0.1s.gif")
        img22 = pygame.image.load("gameart/coinframes/frame_21_delay-0.1s.gif")
        img23 = pygame.image.load("gameart/coinframes/frame_22_delay-0.1s.gif")
        img24 = pygame.image.load("gameart/coinframes/frame_23_delay-0.1s.gif")

        img1 = pygame.transform.scale(img1, (width, height))
        img2 = pygame.transform.scale(img2, (width, height))
        img3 = pygame.transform.scale(img3, (width, height))
        img4 = pygame.transform.scale(img4, (width, height))
        img5 = pygame.transform.scale(img5, (width, height))
        img6 = pygame.transform.scale(img6, (width, height))
        img7 = pygame.transform.scale(img7, (width, height))
        img8 = pygame.transform.scale(img8, (width, height))
        img9 = pygame.transform.scale(img9, (width, height))
        img10 = pygame.transform.scale(img10, (width, height))
        img11 = pygame.transform.scale(img11, (width, height))
        img12 = pygame.transform.scale(img12, (width, height))
        img13 = pygame.transform.scale(img13, (width, height))
        img14 = pygame.transform.scale(img14, (width, height))
        img15 = pygame.transform.scale(img15, (width, height))
        img16 = pygame.transform.scale(img16, (width, height))
        img17 = pygame.transform.scale(img17, (width, height))
        img18 = pygame.transform.scale(img18, (width, height))
        img19 = pygame.transform.scale(img19, (width, height))
        img20 = pygame.transform.scale(img20, (width, height))
        img21 = pygame.transform.scale(img21, (width, height))
        img22 = pygame.transform.scale(img22, (width, height))
        img23 = pygame.transform.scale(img23, (width, height))
        img24 = pygame.transform.scale(img24, (width, height))

        self.img = img1

        self.img_list = [img1, img1, img1,img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12,
                    img13, img14, img15, img16, img17, img18, img19, img20, img21, img22, img23, img24]

        self.count = 0
        self.frame = 0

    def move(self, speed):
        self.x += speed
        self.rect = pygame.Rect((self.x -10, self.y -10), (self.radious, self.radious))

    def animate(self):
        self.count += 1
        if self.count == 5:
            self.count = 0
            self.frame += 1
            if self.frame == len(self.img_list):
                self.frame = 0
            self.img = self.img_list[self.frame]