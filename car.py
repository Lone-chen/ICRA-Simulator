class car(object):
    def __init__(self, bullet, angle, yaw, pitch, buff=0, hp=2000, heat=0, local=(0, 0)):
        self.T = 0.1                # 循环周期 -> 0.1s
        self.HEAT_FREEZE = -120     # 每秒冷却速度
        self.hp = hp                # 小车血量
        self.bullet = bullet
        self.heat = heat
        self.x = local(0)
        self.y = local(1)
        self.angle = angle
        self.yaw = yaw
        self.pitch = pitch
        self.buff = buff
        self.inSight = [0,0]        # 敌方车辆是否在视野内 0->不在 1->在

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

    def change_heat(self, v):  # 每次行动都应调用
        self.heat += v
        if self.hp >= 400:
            if (self.heat > 240) and (self.heat < 360):
                burned = -4 * (self.heat - 240)
                self.hp += burned
                self.heat += self.HEAT_FREEZE * self.T
                # 计算周期扣除血量
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
                # 计算周期扣除血量
            elif self.heat >= 360:
                burned = -40 * (self.heat - 360)
                self.hp += burned
                self.heat = 360
            else:
                self.heat = max(0, self.heat + 2 * self.HEAT_FREEZE * self.T)

    def change_local(self, change):
        self.x += change(0)
        self.y += change(1)

    def change_angle(self, change):
        self.angle += change

    def change_yaw(self, change):
        self.yaw += change

    def change_pitch(self, change):
        self.pitch += change

    def change_buff(self, change):
        self.buff = change
        # 0为无buff
