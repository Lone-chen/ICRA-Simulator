from main.car import CAR
from main.input_output import observation,action
from main.map import MAP
import main.rewardfunction as rf
import random
import math


class ver_env(object):
    def __init__(self):
        self.carA = CAR(0, 50, 0, 0, local=(398, 50))
        self.carB = CAR(1, 50, math.pi/2, 0, local=(799, 50))
        self.map = MAP()
        self.Afire = 0
        self.Bfire = 0
        self.time = 1800
        self.done = 0
        self.inf = -10000
        self.build_match()
        self.chufa = [0, 0, 0, 0, 0, 0]
        self.old_sA = observation()
        self.old_sB = observation()


    def build_match(self):
        pass

    def reset(self):
        self.carA.reset()
        self.carB.reset()
        self.map.areas_rand()
        self.Afire = 0
        self.Bfire = 0
        self.time = 1800
        self.done = 0
        sA = observation(self.carA.hp, self.carA.bullet, self.carA.heat, self.Afire,
                         self.carA.pitch, self.carA.debuff, self.carA.x, self.carA.y,
                         self.carA.line_speed, self.carA.angular_speed,
                         self.carB.hp, self.carB.bullet, self.carB.heat,
                         self.get_car_x(self.carB), self.get_car_y(self.carB),
                         self.carB.isdetected, 0, self.time)
        sB = observation(self.carB.hp, self.carB.bullet,self.carB.heat, self.Bfire,
                         self.carB.pitch, self.carB.debuff, self.carB.x, self.carB.y,
                         self.carB.line_speed, self.carB.angular_speed,
                         self.carA.hp, self.carA.bullet,self.carA.heat,
                         self.get_car_x(self.carA), self.get_car_y(self.carA),
                         self.carA.isdetected, 0, self.time)
        self.old_sA = sA
        self.old_sB = sB
        return sA.get_observation(), sB.get_observation()

    def step(self, actionA, actionB):
        # 未定义碰撞
        actionA = action(actionA)
        actionB = action(actionB)
        sA = observation()
        sB = observation()
        self.carA.change_location(actionA.linear_vel, actionA.angle_vel, actionA.w)
        self.carB.change_location(actionB.linear_vel, actionB.angle_vel, actionA.w)
        self.carA.get_isdetected()
        self.carB.get_isdetected()

        sA.myx = self.carA.x
        sA.myy = self.carA.y
        sA.mytheta = self.carA.angle
        sA.mylinearvel = self.carA.line_speed
        sA.myanglevel = self.carA.angular_speed
        sA.enemyx = self.get_car_x(self.carB)
        sA.enemyy = self.get_car_y(self.carB)
        sA.detected = self.carB.isdetected
        sA.canattack = self.carA.visual_field(self.carB)
        sA.myfire = self.Afire

        sB.myx = self.carB.x
        sB.myy = self.carB.y
        sB.mytheta = self.carB.angle
        sB.mylinearvel = self.carB.line_speed
        sB.myanglevel = self.carB.angular_speed
        sB.enemyx = self.get_car_x(self.carA)
        sB.enemyy = self.get_car_y(self.carA)
        sB.detected = self.carA.isdetected
        sB.canattack = self.carB.visual_field(self.carA)
        sB.myfire = self.Bfire

        if actionA.fire == 1:
            self.carA.attack(self.carB)
            self.Afire = 1
        else:
            self.Afire = 0

        if actionB.fire == 1:
            self.carB.attack(self.carA)
            self.Bfire = 1
        else:
            self.Bfire = 0

        self.check_on_buff(self.carA)
        self.check_on_buff(self.carB)

        rA = rf.reward(self.old_sA, sA)
        rB = rf.reward(self.old_sA, sA)
        if self.carA.on_barriers() == 1:
            self.done = 1
            rA = self.inf
        if self.carB.on_barriers() == 1:
            self.done = 1
            rB = self.inf
        if self.time == 0:
            self.done = 1
        self.old_sA = sA
        self.old_sB = sB
        self.time -= 1
        return sA.get_observation(), rA, sB.get_observation(), rB, self.done

    def get_car_x(self, carx):
        if carx.isdected == 1 and carx.canattack == 1:
            return carx.x
        elif carx.isdected == 1 and carx.canattack == 0:
            return carx.x + 400 * random.uniform(-0.03, 0.03)
        else:
            return -1
    def get_car_y(self, carx):
        if carx.isdected == 1 and carx.canattack == 1:
            return carx.y
        elif carx.isdected == 1 and carx.canattack == 0:
            return carx.y + 250 * random.uniform(-0.03, 0.03)
        else:
            return -1
    def check_on_buff(self, carx):
        pass
