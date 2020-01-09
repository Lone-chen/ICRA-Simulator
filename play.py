from main.car import CAR
from main.input_output import observation,action
from main.map import MAP
import main.rewardfunction

class ver_env(object):
    def __init__(self):
        carA = CAR(0,50,0)
        carB = CAR()
        map = MAP()

        self.build_match()


    def build_match(self):
        pass