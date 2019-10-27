T = 0.1 #s
HEAT_FREEZE = -120  # 每秒
HEAT_FREEZE_ = -240  # 血量低于400

class car(object):
    def __init__(self, bullet, angle, yaw, pitch, buff=0, hp=2000, heat=0, can_shoot=True, local=(0, 0)):
        self.hp = hp
        self.bullet = bullet
        self.heat = heat
        self.can_shoot = can_shoot
        self.x = local(0)
        self.y = local(1)
        self.angle = angle
        self.yaw = yaw
        self.pitch = pitch
        self.buff = buff

    def v_punishment(self,v,bullet_shoot):
        punishment = 0
        if v >= 35:
            punishment = -2000 * bullet_shoot
        elif (v < 35) and (v >= 30):
            punishment = -1000 * bullet_shoot
        elif (v < 30) and (v > 25):
            punishment = -200 * bullet_shoot
        self.hp+=punishment

    def attacked(self,attacked,crash):
        change=0
        if attacked == 0:
            change += -20 -10*crash
        elif attacked == 1:
            change += -40 -10*crash
        elif attacked == 2:
            change += -60 -10*crash
        self.hp+=change

    def change_bullet(self, change):
        self.bullet += change

    def change_heat(self, v):  # 每次子弹发射都应调用
        self.heat += v
        if self.hp >= 400:
            if (self.heat > 240) and (self.heat < 360):
                burned = -4 * (self.heat - 240)
                self.hp += burned
                self.heat += HEAT_FREEZE*T
                # 计算周期扣除血量
            if self.heat >= 360:
                burned = -40 * (self.heat - 360)
                self.hp += burned
                self.heat = 360
        else:
            if (self.heat > 240) and (self.heat < 360):
                burned = -4 * (self.heat - 240)
                self.hp += burned
                self.heat += HEAT_FREEZE_*T
                # 计算周期扣除血量
            if self.heat >= 360:
                burned = -40 * (self.heat - 360)
                self.hp += burned
                self.heat = 360

    def change_canshoot(self, change):
        self.can_shoot += change

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
