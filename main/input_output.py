class observation(object):
    def __init__(self, myhp=0, mybullet=0, myheat=0, myfire=0,
                 mypitch=0, mydebeff=0, myx=0, myy=0, mytheta=0,
                 mylinearvel=0, myanglevel=0,
                 enemyhp=0, enemybullet=0, enemyheat=0, enemyx=0, enemyy=0,
                 detected=0, canattack=0, remaintime=0):
        self.myhp = myhp
        self.mybullet = mybullet
        self.myheat = myheat
        self.myfire = myfire
        self.mypitch = mypitch
        self.mydebeff = mydebeff
        self.myx = myx
        self.myy = myy
        self.mytheta = mytheta
        self.mylinearvel = mylinearvel
        self.myanglevel = myanglevel
        self.enemyhp = enemyhp
        self.enemybullet = enemybullet
        self.enemyheat = enemyheat
        self.enemyx = enemyx
        self.enemyy = enemyy
        self.detected = detected
        self.canattack = canattack
        self.remaintime = remaintime
        self.chufa = [0, 0, 0, 0, 0, 0]


    def get_observation(self):
        return [self.myhp, self.mybullet, self.myheat, self.myfire,
                self.mypitch, self.mydebeff, self.myx, self.myy,
                self.mytheta, self.mylinearvel, self.myanglevel,
                self.enemyhp, self.enemybullet, self.enemyheat,
                self.enemyx, self.enemyy, self.isdetected,
                self.canattack, self.remaintime,
                self.chufa[2], self.chufa[3], self.chufa[4], self.chufa[5]]


class action(object):
    def __init__(self, actions):
        self.linear_vel = actions[0]
        self.angle_vel = actions[1]
        self.w = action[2]
        self.fire = actions[3]
