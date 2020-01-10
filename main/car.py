import math
import random
from main.map import MAP
import main.get_line
import main.action
import main.visual_judge


class CAR(object):
    def __init__(self, team, bullet, angle, pitch, hpbuff=0, bulletbuff=0, debuff=0, hp=2000, heat=0, local=(300, 300)):
        self.T = 0.1                # 循环周期 -> 0.1s
        self.team = team            # 0为红方，1为蓝方
        self.HEAT_FREEZE = -120     # 每秒冷却速度
        self.hp = hp                # 小车血量
        self.bullet = bullet        # 子弹数
        self.heat = heat            # 枪管热量
        self.x = local[0]           # 横坐标
        self.y = local[1]           # 纵坐标
        self.angle = angle          # 绝对角度
        self.line_acel = 0          # 线加速度
        self.angular_acel = 0       # 角加速度
        self.line_speed = 0         # 线速度
        self.angular_speed = 0      # 角速度
        self.carLength = 600        # 纵向长度
        self.carWidth = 450         # 横向长度
        # self.yaw = yaw
        self.pitch = pitch          # 炮台水平角度
        self.hpbuff = hpbuff        # 加血buff
        self.bulletbuff = bulletbuff  # 补弹buff
        self.debuff = debuff            # 禁区buff时间
        self.isdetected = self.get_isdetected()         # 小车是否被敌方观察到
        self.carLength = 600  # 纵向长度
        self.carWidth = 450  # 横向长度
        self.peak = self.get_peak() # 小车顶点数组
        self.inSight = [0, 0, 0, 0]       # 敌方车辆是否在视野内 0->不在 1->在
        self.armors = [[], [], [], [], [], [], [], []]    # 装甲板相对小车中心距离,前后左右
        self.reset_data = [local[0], local[1], angle, pitch]
        self.v = 20                 # 子弹发射速度
        self.w_vel = math.pi        # 炮台旋转速度

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
        ：param attacked：被击中的装甲编号 0->正面装甲 1->背面装甲 2->侧面装甲
        : param crash: 装甲撞击到护栏的次数
        """
        change = 0
        if attacked == 0:
            change += -20 -10*crash
        elif attacked == 1:
            change += -60 -10*crash
        elif attacked == 2:
            change += -40 -10*crash
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
        return self.angle

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

    def get_peak(self):
        peak = [self.x - self.carWidth / 2, self.y - self.carLength / 2,
                self.x + self.carWidth / 2, self.y - self.carLength / 2,
                self.x + self.carWidth / 2, self.y + self.carLength / 2,
                self.x - self.carWidth / 2, self.y + self.carLength / 2]
        return peak

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
        L = self.carLength / 2 # 中心距边长的值
        W = self.carWidth / 2
        # 从左上角为1开始标记，依次依据公式计算四个顶点的坐标，顺时针
        self.peak[0] = int((self.peak[0] - self.x) * math.cos(self.angle) - ((self.peak[1] - self.y)*math.sin(self.angle))) + self.x
        self.peak[1] = int((self.peak[0] - self.x) * math.sin(self.angle) + ((self.peak[1] - self.y) * math.cos(self.angle))) + self.y
        self.peak[2] = int((self.peak[2] - self.x) * math.cos(self.angle) - ((self.peak[3] - self.y)*math.sin(self.angle))) + self.x
        self.peak[3] = int((self.peak[2] - self.x) * math.sin(self.angle) + ((self.peak[3] - self.y) * math.cos(self.angle))) + self.y
        self.peak[4] = int((self.peak[4] - self.x) * math.cos(self.angle) - ((self.peak[5] - self.y)*math.sin(self.angle))) + self.x
        self.peak[5] = int((self.peak[4] - self.x) * math.sin(self.angle) + ((self.peak[5] - self.y) * math.cos(self.angle))) + self.y
        self.peak[6] = int((self.peak[6] - self.x) * math.cos(self.angle) - ((self.peak[7] - self.y)*math.sin(self.angle))) + self.x
        self.peak[7] = int((self.peak[6] - self.x) * math.sin(self.angle) + ((self.peak[7] - self.y) * math.cos(self.angle))) + self.y

    def reset(self):
        """
        重置小车属性
        :return:
        """
        self.hp = 2000
        self.x = self.reset_data[0]
        self.y = self.reset_data[1]
        self.bullet = 50
        self.heat = 0
        self.angle = self.reset_data[2]
        self.pitch = self.reset_data[3]
        self.hpbuff = 0
        self.bulletbuff = 0
        self.debuff = 0
        self.peak = self.get_peak()
        self.inSight = [0, 0]
        self.armors = [[], [], [], [], [], [], [], []]
        self.line_speed = 0
        self.angular_speed = 0
        self.line_acel = 0
        self.angular_speed = 0
        self.mp = MAP()

    def change_location(self, l_speed, angle_speed):
        """

        :param l_acel: 小车的线速度
        :param angle_acel: 小车的角速度
        :return:
        """
        self.x = 0
        self.y = 0
        self.line_speed += self.line_acel * self.T
        self.angular_speed +=  self.angular_speed * self.T

    def get_isdetected(self):
        if random.random() >= 0.7:
            return 1
        else:
            return 0

    def visual_field(self, A):
        """
        判断小车装甲板是否在视野内
        :param A: 一个小车对象
        :return: 哪个光条被看见
        """
        m = []
        for i in range(0, 8):
            for j in range(0, 4):
                m[i] = main.action.is_inter(A.peak[j], A.peak[j+1], A.armors[i], [self.x, self.y])
                if m[i] == 1:
                    break

        if m[0] == 0 and m[1] == 0 and main.visual_judge.visual(A.armors[0][0], A.armors[0][1], A.armors[1][0], A.armors[1][1], self.x, self.y, self.angle, self.pitch):
            self.inSight[0] = 1
        if m[2] == 0 and m[3] == 0 and main.visual_judge.visual(A.armors[2][0], A.armors[2][1], A.armors[3][0], A.armors[3][1], self.x, self.y, self.angle, self.pitch):
            self.inSight[1] = 1
        if m[4] == 0 and m[5] == 0 and main.visual_judge.visual(A.armors[4][0], A.armors[4][1], A.armors[5][0], A.armors[5][1], self.x, self.y, self.angle, self.pitch):
            self.inSight[2] = 1
        if m[6] == 0 and m[7] == 0 and main.visual_judge.visual(A.armors[6][0], A.armors[6][1], A.armors[7][0], A.armors[7][1], self.x, self.y, self.angle, self.pitch):
            self.inSight[3] = 1

        if self.inSight[1] == 1:
            return 2
        if self.inSight[2] == 1:
            return 3
        if self.inSight[3] == 1:
            return 3
        if self.inSight[0] == 1:
            return 1
        return 0

    def attack(self, carx):
        """
        攻击判定函数
        """
        xA = self.visual_field(carx)
        self.change_bullet(-1)  # A子弹减少
        self.change_heat(self.v)  # A枪口热量增加
        if xA == 0:  # A不能看见B
            self.change_pitch(0)  # A炮台旋转角不变
        else:
            self.change_pitch(0)  # A炮台旋转角不变
            carx.attacked(xA - 1, 0)

    def aiming(self, carx):
        if carx.isdetected or max(carx.inSight):
            dir_angle = math.atan2(carx.y - self.y, carx.x - self.x) - self.angle
            if abs(dir_angle - self.angle) > self.w_vel:
                self.angle += dir_angle / abs(dir_angle) * self.w_vel
            else:
                self.angle += dir_angle


