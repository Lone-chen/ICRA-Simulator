from car import CAR

car1 = CAR()
car2 = CAR()


class state(object):
    def __init__(self, hp_1, bullet_1, heat_1, pitch_1,
                 x_1, y_1, hp_2, bullet_2, heat_2 ,pitch_2, x_2, y_2):
        self.myhp = hp_1
        self.mybullet = bullet_1
        self.mtheat = heat_1
        self.fired = 0  # 0为未开火，1为开火
        self.mypitch = pitch_1
        self.mydebuff = 0
        self.my_x = x_1
        self.my_y = y_1
        self.theta = 0
        self.linear_val = 0
        self.angle_val = 0

        self.enemyhp = hp_2
        self.enemybullet = bullet_2
        self.enemyheat = heat_2
        self.enemypitch = pitch_2
        self.enemydebuff = 0
        self.enemy_x = x_2
        self.enemy_y = y_2
        self.isDetected = 0  # 0为未被侦测，1为被侦测

        self.time = 180


class action(object):
    def __init__(self):
        self.x = 0  # 0-810
        self.y = 0  # 0-510
        self.fire = 0  # 0:不发射，1：发射


def step(self, action):



