import pygame
from random import randint
from Coin import Coin
from random import uniform

class PickUpHandler():

    def __init__(self, pickup_list):
        self.oblist = pickup_list
        self.coinrate = 60*5
        self.count = 0

    def decide(self):
        return self.oblist[randint(0, len(self.oblist) -1)]

    def spawn(self):

        ob = self.decide()
        if ob == "coin":
            y = randint(20, 700)
            coin = Coin(1340, y)
            return coin
