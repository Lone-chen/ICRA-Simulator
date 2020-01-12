import math
import random
from main.map import MAP
import main.get_line

C = MAP()


def angle_calculate(x, y):
    """
    计算角度
    :param x: 边长x
    :param y: 边长y
    :return: 角度
    """
    xl = math.hypot(x, y)
    return math.asin(y / xl)


def barrier_visual(x, y, x_car, y_car):
    """
    判断光条是否被障碍物阻挡
    :param (x, y): 光条坐标
    :param (x_car, y_car): 小车坐标
    :return: 0 或 1
    """
    list = main.get_line.get_lines(x, y, x_car, y_car)
    for i, j in list:
        if C.map[i][j] == 1:
            return 0
    return 1  # 光条未被障碍物阻挡则返回1


def visual(x1, y1, x2, y2, x_car, y_car, angle, pitch):
    """
    小车视野判定
    (x1,y1)和(x2,y2)为光条坐标
    (x_car,y_car)为小车坐标
    :param angle: 底盘旋转角
    :param pitch: 炮台水平转角
    """
    _sign1 = 1  # 光条1是否在视野内的标志变量
    _sign2 = 1  # 光条2是否在视野内的标志变量
    X1,Y1 = abs(x1-x_car) , abs(y1-y_car)
    X2,Y2 = abs(x2-x_car) , abs(y2-y_car)

    if abs(angle_calculate(X1, Y1) - angle - pitch) <= 5 * math.pi / 12 and abs(angle_calculate(X2, Y2) - angle - pitch) <= 5 * math.pi / 12:  # 两个光条是否在视野内
        _sign1 = barrier_visual(x1, y1, x_car, y_car)
        _sign2 = barrier_visual(x2, y2, x_car, y_car)
        if _sign1 == 1 and _sign2 == 1:
            return 1
        else:
            return 0



