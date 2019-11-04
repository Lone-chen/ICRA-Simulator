from map import MAP
import math


class CAR(object):
    def __init__(self, bullet, angle, yaw, pitch, peak, buff=0, hp=2000, heat=0, local=(300, 300)):
        self.T = 0.1                # 循环周期 -> 0.1s
        self.HEAT_FREEZE = -120     # 每秒冷却速度
        self.hp = hp                # 小车血量
        self.bullet = bullet        # 子弹数
        self.heat = heat            # 枪管热量
        self.x = local[0]           # 横坐标
        self.y = local[1]           # 纵坐标
        self.angle = angle          # 绝对角度
        self.yaw = yaw              # 炮台水平角度
        self.buff = buff            # 禁区buff
        self.peak = peak            # 小车顶点数组
        self.inSight = [0, 0]       # 敌方车辆是否在视野内 0->不在 1->在
        self.carLength = 600        # 纵向长度
        self.carWidth = 450         # 横向长度
        self.armors = [(),(),(),(),(),(),(),()]    # 装甲板相对小车中心距离

    def v_punishment(self, v):
        """
        计算子弹发射超速惩罚
        :param v: 子弹发射速度
        """
        punishment = 0
        if v >= 35:
            punishment = -2000
        elif (v < 35) and (v >= 30):
            punishment = -1000
        elif (v < 30) and (v > 25):
            punishment = -200
        self.hp += punishment

    def attacked(self,attacked,crash):
        """
        计算冲击扣除血量
        ：param attacked：被击中的装甲编号 0->正面装甲 1->侧面装甲 2->背面装甲
        : param crash: 装甲撞击到护栏的次数
        """
        change = 0
        if attacked == 0:
            change += -20 -10*crash
        elif attacked == 1:
            change += -40 -10*crash
        elif attacked == 2:
            change += -60 -10*crash
        self.hp += change

    def change_bullet(self, change):
        self.bullet += change

    def change_heat(self, v):
        """
        计算枪口热量的冷却和过热惩罚
        ：param v:子弹速度
        """
        self.heat += v
        if self.hp >= 400:
            if (self.heat > 240) and (self.heat < 360):
                burned = -4 * (self.heat - 240)
                self.hp += burned
                self.heat += self.HEAT_FREEZE * self.T
                # 计算正常血量下每周期扣除血量
            elif self.heat >= 360:
                burned = -40 * (self.heat - 360)
                self.hp += burned
                self.heat = 360
            else:
                self.heat = max(0, self.heat + self.HEAT_FREEZE * self.T)
        else:
            if (self.heat > 240) and (self.heat < 360):
                burned = -4 * (self.heat - 240)
                self.hp += burned
                self.heat += 2 * self.HEAT_FREEZE * self.T
                # 计算低血量（hp少于400）下每周期扣除血量
            elif self.heat >= 360:
                burned = -40 * (self.heat - 360)
                self.hp += burned
                self.heat = 360
            else:
                self.heat = max(0, self.heat + 2 * self.HEAT_FREEZE * self.T)

    def change_local(self, change):
        """
        计算机器人坐标的变化
        ：param change：x、y坐标的变化量
        """
        self.x += change(0)
        self.y += change(1)

    def change_angle(self, change):
        """
        计算机器人底盘的变化
        ：param change：地盘绝对角度的变化量
        """
        self.angle += change

    def change_yaw(self, change):
        """
        计算机器人炮塔仰角的变化
        ：param change：仰角的变化量
        """
        self.yaw += change

    def change_pitch(self, change):
        """
        计算机器人炮塔旋转角的变化
        ：param change：旋转角的变化量
        """
        self.pitch += change

    def change_buff(self, change):
        """
        :param buff:加成效果
        0->buff,1->回血，2->弹药补给，3->禁止移动
        """
        self.buff = change

    def covered_area(self):
        """
        计算机器人的投影面积
        点旋转计算公式：
        srx = (x-pointx)*cos(angle) + (y-pointy)*sin(angle)+pointx
        sry = (y-pointy)*cos(angle) - (x-pointx)*sin(angle)+pointy
        nrx = (x-pointx)*cos(angle) - (y-pointy)*sin(angle)+pointx
        nry = (x-pointx)*sin(angle) + (y-pointy)*cos(angle)+pointy
        :param MAP: map地图
        :return:
        """
        L = 300 # 中心距边长的值
        # 从左上角为1开始标记，依次依据公式计算四个顶点的坐标
        if self.angle >= 0:
            self.peak[0] = math.ceil(-L * math.acos(self.angle) + L*math.asin(self.angle)) + self.x
            self.peak[1] = math.ceil(L * math.acos(self.angle) -(-L * math.asin(self.angle)) ) + self.y
            self.peak[2] = math.ceil(L * math.cos(self.angle) + L * math.asin(self.angle)) + self.x
            self.peak[3] = math.ceil(L * math.acos(self.angle) - L * math.asin(self.angle)) + self.y
            self.peak[4] = math.ceil(L * math.acos(self.angle) + (-L * math.sin(self.angle))) + self.x
            self.peak[5] = math.ceil(-L * math.acos(self.angle) - L * math.asin(self.angle)) + self.y
            self.peak[6] = math.ceil(-L * math.acos(self.angle) + (-L * math.asin(self.angle))) + self.x
            self.peak[7] = math.ceil(-L * math.acos(self.angle) - (-L * math.asin(self.angle))) + self.y
        elif self.angle < 0:
            self.peak[0] = math.ceil(-L * math.acos(self.angle) - L * math.asin(self.angle)) + self.x
            self.peak[1] = math.ceil(L * math.acos(self.angle) + (-L * math.asin(self.angle))) + self.y
            self.peak[2] = math.ceil(L * math.cos(self.angle) - L * math.asin(self.angle)) + self.x
            self.peak[3] = math.ceil(L * math.acos(self.angle) + L * math.asin(self.angle)) + self.y
            self.peak[4] = math.ceil(L * math.acos(self.angle) - (-L * math.sin(self.angle))) + self.x
            self.peak[5] = math.ceil(-L * math.acos(self.angle) + L * math.asin(self.angle)) + self.y
            self.peak[6] = math.ceil(-L * math.acos(self.angle) - (-L * math.asin(self.angle))) + self.x
            self.peak[7] = math.ceil(-L * math.acos(self.angle) + (-L * math.asin(self.angle))) + self.y

