from main.car import CAR
from main.input_output import observation,action
from main.map import MAP
import main.rewardfunction
import random


class ver_env(object):
    def __init__(self):
        self.carA = CAR(0, 50, 0, 0, local=(398, 50))
        self.carB = CAR(1, 50, 180, 0, local=(799, 50))
        self.map = MAP()

        self.build_match()


    def build_match(self):
        pass

    def reset(self):
        self.carA.reset()
        self.carB.reset()
        self.map.areas_rand()
        sA = observation(self.carA.hp, self.carA.bullet, self.carA.heat, 0,
                         self.carA.pitch, self.carA.debuff, self.carA.x, self.carA.y,
                         0, 0,
                         self.carB.hp, self.carB.bullet, self.carB.heat, self.carB.x, self.carB.y,
                         self.get_isdetected(), 0, 1800)
        sB = observation(self.carB.hp, self.carB.bullet,self.carB.heat, 0,
                         self.carB.pitch, self.carB.debuff, self.carB.x, self.carB.y,
                         0, 0,
                         self.carA.hp, self.carA.bullet,self.carA.heat, self.carA.x, self)
        return sA, sB

    def step(self):
        pass

    def get_isdetected(self):
        if random.random() >= 0.7:
            return 1
        else:
            return 0
