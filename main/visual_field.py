import math
import random
from main.car import CAR
from main.map import MAP
import main.get_line

C = MAP()
A = CAR(50,0,0,0,0)
B = CAR(50,0,0,0,0)


def angle_calculate(x, y):
    """
    计算角度
    :param x: 边长x
    :param y: 边长y
    :return: 角度
    """
    xl = math.hypot(x, y)
    return math.asin(y / xl) * 180 / math.pi


def barrier_visual(x,y,x_car,y_car):
    """
    判断光条是否被障碍物阻挡
    :param (x, y): 光条坐标
    :param (x_car, y_car): 小车坐标
    :return: 0 或 1
    """
    list = main.get_line.get_lines(x, y, x_car, y_car)
    for i, j in list:
        if C.map[i][j] == 1:
            return 1
    return 0  # 光条未被障碍物阻挡则返回0


def visual_field(x1,y1,x2,y2,x_car,y_car,angle,pitch):
    """
    小车视野判定
    (x1,y1)和(x2,y2)为光条坐标
    (x_car,y_car)为小车坐标
    :param angle: 底盘旋转角
    :param pitch: 炮台水平转角
    """
    _sign1 = 0  # 光条1是否在视野内的标志变量
    _sign2 = 0  # 光条2是否在视野内的标志变量
    X1,Y1 = abs(x1-x_car) , abs(y1-y_car)
    X2,Y2 = abs(x2-x_car) , abs(y2-y_car)

    if abs(angle_calculate(X1, Y1) - angle - pitch) <= 75 and abs(angle_calculate(X2, Y2) - angle - pitch) <= 75:  # 两个光条是否在视野内
        _sign1 = barrier_visual(x1, y1, x_car, y_car)
        _sign2 = barrier_visual(x2, y2, x_car, y_car)
        if _sign1 == 0 and _sign2 == 0:
            return 0
        else:
            return 1


def attack(A, B):
    """
    攻击判定函数
    :param A: 小车A
    :param B: 小车B
    """
    xA = visual_field(0, 0, 0, 0, 0, 0, 0, 0)
    xB = visual_field(0, 0, 0, 0, 0, 0, 0, 0)
    if xA == 1:  # A不能看见B,并且攻击
        A.change_bullet(-1)  # A子弹减少
        A.change_heat(0)  # A枪口热量增加
        A.change_pitch(0)  # A炮台旋转角不变
        B.attacked(0, 0)  # B不掉血

    if xA == 0:  # A能看见B,并且攻击
        A.change_bullet(-1)  # A子弹减少
        A.change_heat(0)  # A枪口热量增加
        A.change_pitch(0)  # A炮台旋转角变化,对准光条中间
        i = random.randint(1,2)
        if i == 1:
            B.attacked(0, 0)  # 概率掉血

    if xB == 1:  # B不能看见A,并且攻击
        B.change_bullet(-1)
        B.change_heat(0)
        B.change_pitch(0)
        A.attacked(0, 0)

    if xB == 0:  # B能看见A,并且攻击
        B.change_bullet(-1)
        B.change_heat(2)
        B.change_pitch(0)
        i = random.randint(1, 2)
        if i == 1:
            A.attacked(0, 0)
