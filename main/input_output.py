class observation(object):
    def __init__(self, myhp=0, mybullet=0, myheat=0, myfire=0,
                 mypitch=0, mydebuff_move=0, mydebuff_shoot=0, myx=0, myy=0, mytheta=0,
                 mylinearvel=0, myanglevel=0,
                 enemyhp=0, enemybullet=0, enemyx=0, enemyy=0,
                 isdetected=0, canattack=0, remaintime=0):
        self.myhp = myhp
        self.mybullet = mybullet
        self.myheat = myheat
        self.myfire = myfire
        self.mypitch = mypitch
        self.mydebeff_move = mydebuff_move
        self.mydebeff_shoot = mydebuff_shoot
        self.myx = myx
        self.myy = myy
        self.mytheta = mytheta
        self.mylinearvel = mylinearvel
        self.myanglevel = myanglevel
        self.enemyhp = enemyhp
        self.enemybullet = enemybullet
        self.enemyx = enemyx
        self.enemyy = enemyy
        self.isdetected = isdetected
        self.canattack = canattack
        self.remaintime = remaintime
        self.chufa = [0, 0, 0, 0, 0, 0] # x-2
        self.area_x = [0, 0, 0, 0, 0, 0]
        self.area_y = [0, 0, 0, 0, 0, 0]

    def get_observation(self):
        return [self.myhp, self.mybullet, self.myheat, self.myfire,
                self.mypitch, self.mydebeff_move, self.mydebeff_shoot, self.myx, self.myy,
                self.mytheta, self.mylinearvel, self.myanglevel,
                self.enemyhp, self.enemybullet,
                self.enemyx, self.enemyy, self.isdetected,
                self.canattack, self.remaintime,
                self.chufa[0], self.chufa[1], self.chufa[2], self.chufa[3], self.chufa[4], self.chufa[5],
                self.area_x[0], self.area_x[1], self.area_x[2], self.area_x[3], self.area_x[4], self.area_x[5],
                self.area_y[0], self.area_y[1], self.area_y[2], self.area_y[3], self.area_y[4], self.area_y[5]]


class action(object):
    def __init__(self, actions):
        self.linear_vel = actions[0]
        self.angle_vel = actions[1]
        self.w = action[2]
        self.fire = actions[3]
