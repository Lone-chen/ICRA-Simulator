from main.car import CAR
from main.input_output import observation,action
from main.map import MAP
import main.rewardfunction as rf
import random
import math


class ver_env(object):
    def __init__(self):
        self.map = MAP()
        self.carA = CAR(0, 50, 0, 0, self.map, local=(398, 50))
        self.carB = CAR(1, 50, math.pi/2, 0,self.map, local=(799, 50))

        self.Afire = 0
        self.Bfire = 0
        self.time = 1800
        self.done = 0
        self.inf = -10000
        self.build_match()
        self.chufa = [0, 0, 0, 0, 0, 0]
        self.area_x = [0, 0, 0, 0, 0, 0]
        self.area_y = [0, 0, 0, 0, 0, 0]
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
                         self.get_car_x(self.carA, self.carB), self.get_car_y(self.carA, self.carB),
                         self.carB.isdetected, 0, self.time)
        sB = observation(self.carB.hp, self.carB.bullet,self.carB.heat, self.Bfire,
                         self.carB.pitch, self.carB.debuff, self.carB.x, self.carB.y,
                         self.carB.line_speed, self.carB.angular_speed,
                         self.carA.hp, self.carA.bullet,self.carA.heat,
                         self.get_car_x(self.carB, self.carA), self.get_car_y(self.carB, self.carA),
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
        sA.enemyx = self.get_car_x(self.carA, self.carB)
        sA.enemyy = self.get_car_y(self.carA, self.carB)
        sA.isdetected = self.carB.isdetected
        sA.canattack = self.carA.visual_field(self.carB)
        sA.myfire = self.Afire

        sB.myx = self.carB.x
        sB.myy = self.carB.y
        sB.mytheta = self.carB.angle
        sB.mylinearvel = self.carB.line_speed
        sB.myanglevel = self.carB.angular_speed
        sB.enemyx = self.get_car_x(self.carB, self.carA)
        sB.enemyy = self.get_car_y(self.carB, self.carA)
        sB.isdetected = self.carA.isdetected
        sB.canattack = self.carB.visual_field(self.carA)
        sB.myfire = self.Bfire

        if self.time == 1800 or self.time == 1200 or self.time == 600:
            self.refresh_buff()
        self.check_on_buff(self.carA)
        self.check_on_buff(self.carB)

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



        sA.myhp = self.carA.hp
        sA.mybullet = self.carA.bullet
        sA.myheat = self.carA.heat
        sA.enemyhp = self.carB.hp
        sA.enemybullet = self.carB.bullet
        sA.mydebeff_shoot = self.carA.shoot_forbiden
        sA.mydebeff_move = self.carA.move_forbiden
        sA.chufa = self.chufa
        sA.area_x = self.area_x
        sA.area_y = self.area_y

        sB.myhp = self.carB.hp
        sB.mybullet = self.carB.bullet
        sB.myheat = self.carB.heat
        sB.enemyhp = self.carA.hp
        sB.enemybullet = self.carA.bullet
        sB.mydebeff_shoot = self.carB.shoot_forbiden
        sB.mydebeff_move = self.carB.move_forbiden
        sB.chufa = self.chufa
        sB.area_x = self.area_x
        sB.area_y = self.area_y

        self.carA.aiming(self.carB)
        sA.mypitch = self.carA.pitch

        self.carB.aiming(self.carA)
        sB.mypitch = self.carB.pitch



        rA = rf.reward(self.old_sA, sA, 0)
        rB = rf.reward(self.old_sB, sB, 1)
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

    def get_car_x(self, carx, cary):
        if cary.isdetected == 1 and carx.visual_field(cary) > 0:
            return cary.x
        elif cary.isdetected == 1 and carx.visual_field(cary) == 0:
            return cary.x + 400 * random.uniform(-0.03, 0.03)
        else:
            return -1
    def get_car_y(self, carx, cary):
        if cary.isdetected == 1 and carx.visual_field(cary) == 1:
            return cary.y
        elif cary.isdetected == 1 and carx.visual_field(cary) == 0:
            return cary.y + 250 * random.uniform(-0.03, 0.03)
        else:
            return -1
    def check_on_buff(self, carx):
        i = carx.on_buff()
        if i == 0:
            return -1
        if self.chufa[i] == 0:
            if i == 2:
                self.carA.hp = min(2000, self.carA.hp + 200)
                self.carA.hpbuff = 1
                self.chufa[i-2] = 1
            if i == 3:
                self.carB.hp = min(2000, self.carB.hp + 200)
                self.carB.hpbuff = 1
                self.chufa[i-2] = 1
            if i == 4:
                self.carA.bullet += 100
                self.carA.bulletbuff = 1
                self.chufa[i-2] = 1
            if i == 5:
                self.carB.bullet += 100
                self.carB.bulletbuff = 1
                self.chufa[i-2] = 1
            if i == 6:
                carx.move_forbiden = 10
                self.chufa[i-2] = 1
            if i == 7:
                carx.shoot_forbiden = 10
                self.chufa[i-2] = 1

    def refreash_buff(self):
        self.map.areas_rand()
        for i in range(0, 6):
            if self.map.areas[i] == 2:
                self.chufa[0] = 0
                self.area_x[0] = (self.map.area_start[0][0] + self.map.area_end[0][0]) / 2
                self.area_y[0] = (self.map.area_start[0][1] + self.map.area_end[0][1]) / 2
            elif self.map.areas[i] == 3:
                self.chufa[1] = 0
                self.area_x[1] = (self.map.area_start[1][0] + self.map.area_end[1][0]) / 2
                self.area_y[1] = (self.map.area_start[1][1] + self.map.area_end[1][1]) / 2
            elif self.map.areas[i] == 4:
                self.chufa[2] = 0
                self.area_x[2] = (self.map.area_start[2][0] + self.map.area_end[2][0]) / 2
                self.area_y[2] = (self.map.area_start[2][1] + self.map.area_end[2][1]) / 2
            elif self.map.areas[i] == 5:
                self.chufa[3] = 0
                self.area_x[3] = (self.map.area_start[3][0] + self.map.area_end[3[0]]) / 2
                self.area_y[3] = (self.map.area_start[3][1] + self.map.area_end[3][1]) / 2
            elif self.map.areas[i] == 6:
                self.chufa[4] = 0
                self.area_x[4] = (self.map.area_start[4][0] + self.map.area_end[4][0]) / 2
                self.area_y[4] = (self.map.area_start[4][1] + self.map.area_end[4][1]) / 2
            elif self.map.areas[i] == 7:
                self.chufa[5] = 0
                self.area_x[5] = (self.map.area_start[5][0] + self.map.area_end[5][0]) / 2
                self.area_y[5] = (self.map.area_start[5][1] + self.map.area_end[5][1]) / 2