from car import CAR
from map import MAP

C = CAR(0, 0, 0, 0, 0)
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


def on_area():
    """
    判断是否接触到障碍区或buff区
    :return:
    """
    for i in range(9):
        if (is_inter(C.peak[0], C.peak[2], M.barrier_start[i], M.barrier_end[i])
                and is_inter(C.peak[1], C.peak[3], M.barrier_start[i], M.barrier_end[i])):
            # 遇到障碍物，改变速度
            pass

    for i in range(6):
        if (is_inter(C.peak[0], C.peak[2], M.area_start[i], M.area_end[i])
                and is_inter(C.peak[1], C.peak[3], M.area_start[i], M.area_end[i])):
            # 遇到buff
            pass
