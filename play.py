from main.car import CAR
from main.input_output import observation,action
from main.map import MAP
import main.rewardfunction

class ver_env(object):
    def __init__(self):
        carA = CAR(0, 50, 0, 0, local=(398, 50))
        carB = CAR(1, 50, 180, 0, local=(799, 50))
        map = MAP()

        self.build_match()


    def build_match(self):
        pass