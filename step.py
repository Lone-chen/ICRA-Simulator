from main.car import CAR
import random, time, threading
from main.map import MAP
import main.rewardfunction

car1 = CAR(0, 0, 0, 0, 0)
car2 = CAR(1, 0, 0, 0, 0)
M = MAP()


def cross(p1, p2, p3):
    """
    跨立实验,判断对角线顶点是否相交叉
    :param p1:
    :param p2:
    :param p3:
    :return:
    """
    x1 = p2[0] - p1[0]
    y1 = p2[1] - p1[1]
    x2 = p3[0] - p1[0]
    y2 = p3[1] - p1[1]
    return x1 * y2 - x2 * y1


def is_inter(p1, p2, p3, p4):
    """
    判断两线段是否相交
    :param p1: L1_1
    :param p2: L1_2
    :param p3: L2_1
    :param p4: L2_2
    :return:
    """
    # 快速排斥，以l1、l2为对角线的矩形必相交，否则两线段不相交
    if (max(p1[0], p2[0]) >= min(p3[0], p4[0])  # 矩形1最右端大于矩形2最左端
            and max(p3[0], p4[0]) >= min(p1[0], p2[0])  # 矩形2最右端大于矩形最左端
            and max(p1[1], p2[1]) >= min(p3[1], p4[1])  # 矩形1最高端大于矩形最低端
            and max(p3[1], p4[1]) >= min(p1[1], p2[1])):  # 矩形2最高端大于矩形最低端

        if (cross(p1, p2, p3) * cross(p1, p2, p4) <= 0
                and cross(p3, p4, p1) * cross(p3, p4, p2) <= 0):
            flag = 1
        else:
            flag = 0
    else:
        flag = 0
    return flag
#  用于判断是否触碰加成区或者禁区

class state(object):
    def __init__(self, hp_1, bullet_1, heat_1, pitch_1,
                 x_1, y_1, hp_2, bullet_2, heat_2 ,pitch_2, x_2, y_2):
        self.myhp = hp_1
        self.mybullet = bullet_1
        self.myheat = heat_1
        self.fired = 0  # 0为未开火，1为开火
        self.mypitch = pitch_1
        self.mydebuff = [0.0, 0.0]  # 第一位为禁止移动区剩余时间， 第二位为禁止发射区剩余时间
        self.my_x = x_1
        self.my_y = y_1
        self.theta = 0
        self.linear_val = 0
        self.angle_val = 0
        self.mybuff_hp = 0
        self.mybuff_bullet = 0  # buff是否被触发

        self.enemyhp = hp_2
        self.enemybullet = bullet_2
        self.enemyheat = heat_2
        self.enemypitch = pitch_2
        self.enemydebuff = [0.0, 0.0]
        self.enemy_x = x_2
        self.enemy_y = y_2
        self.isDetected = 0  # 0为未被侦测，1为被侦测
        self.enebuff_hp = 0
        self.enebuff_bullet = 0  # buff是否被触发

        self.time = 180


class action(object):
    def __init__(self):
        self.x = 0  # 0-810
        self.y = 0  # 0-510
        self.fire = 0  # 0:不发射，1：发射


A = action()
B = state(car1.hp, car1.bullet, car1.heat, car1.pitch, car1.x, car1.y, car2.hp, car2.bullet, car2.heat, car2.pitch, car2.x, car2.y)


def step(A, B, B_primer):
    done = 0
    imformation = 0

    car1.v_punishment(0)
    car1.attacked(0, 0)
    B.myhp = car1.hp
    #  己方小车血量改变

    if B.fired == 0:
        pass
    elif B.fired == 1 and B.isDetected == 1:
        i = random.randint(1, 2)
        if i == 1:
            car2.attacked(1, 0)  # 侦测到并开火，1/2概率掉血
            B.enemyhp = car2.hp
    elif B.fired == 1 and B.isDetected == 0:
        i = random.randint(1, 10)
        if i == 1:
            car2.attacked(1, 0)  # 未看到就开火，1/10概率掉血
            B.enemyhp = car2.hp
    #  根据上一帧是否开火，以及敌方小车是否掉血

    if B.mydebuff[1] == 0:
        if A.fire == 0 :
            car1.change_bullet(0)
            car1.change_heat(0)
            B.fired = 0
        else:
            car1.change_bullet(-1)
            car1.change_heat(20)
            B.fired = 1
    #  根据己方小车是否开火，子弹改变，热量改变

    car1.change_pitch(0)
    B.mypitch = car1.pitch
    #  己方云台水平坐标

    for i in range(0,2):
        if B.mydebuff[i] > 0:
            B.mydebuff[i] = B.mydebuff[i] - 0.1
        else:
            pass
    #  己方小车禁区剩余时间

    B.my_x = A.x
    B.my_y = A.y
    # 己方小车水平坐标，垂直坐标，theta角度，linear_val线速度，angle_val角速度

    for i in range(6):
        if (is_inter([car1.peak[0], car1.peak[1]], [car1.peak[6], car1.peak[7]], M.area_start[i], M.area_end[i])
        or is_inter([car1.peak[2], car1.peak[3]], [car1.peak[4], car1.peak[5]], M.area_start[i], M.area_end[i])):
            if(M.areas[i] == 2):
                B.mybuff_hp = 1
            if(M.areas[i] == 4):
                B.mybuff_bullet = 1
    #  是否触碰加成区和禁区

    if B.enemydebuff[1] == 0:
        car2.change_bullet(0)
        B.enemybullet = car2.bullet
        car2.change_heat(20)
        B.enemyheat = car2.heat
    car2.change_pitch(0)
    B.enemypitch = car2.pitch
    #  敌方小车子弹数，枪口热量，云台水平坐标改变

    for i in range(0,2):
        if B.enemydebuff[i] > 0:
            B.enemydebuff[i] = B.enemydebuff[i] - 0.1
        else:
            pass
    #  敌方小车禁区剩余时间

    for i in range(6):
        if (is_inter([car1.peak[0], car1.peak[1]], [car1.peak[6], car1.peak[7]], M.area_start[i], M.area_end[i])
                or is_inter([car1.peak[2], car1.peak[3]], [car1.peak[4], car1.peak[5]], M.area_start[i],
                            M.area_end[i])):
            if (M.areas[i] == 2):
                B.mybuff_hp = 1
            if (M.areas[i] == 4):
                B.mybuff_bullet = 1
    #  是否触碰加成区和禁区

    B.time = B.time - 0.1
    #  比赛剩余时间

    r = main.rewardfunction.reward(B_primer, B)

    if B.time == 0:
        done = 1

    imformation = 0

    return (B, r, done, imformation)

B_primer = B

for i in range(0, 1800):
    d = step(A, B, B_primer)
    if i != 0:
        B_primer = d[0]
    if d[2] == 1:
        break









