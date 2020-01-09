class observation(object):
    def __init__(self, myhp, mybullet, myheat, myfire,
                 mypitch, mydebeff, myx, myy, mytheta,
                 mylinearvel, myanglevel,
                 enemyhp, enemybullet, enemyheat, enemyx, enemyy,
                 isdetected, canattack, remaintime):
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
        self.isdetected = isdetected
        self.canattack = canattack
        self.remaintime = remaintime


    def get_observation(self):
        return [self.myhp, self.mybullet, self.myheat, self.myfire,
                self.mypitch, self.mydebeff, self.myx, self.myy,
                self.mytheta, self.mylinearval, self.myangleval,
                self.enemyhp, self.enemybullet, self.enemyheat,
                self.enemyx, self.enemyy, self.isdetected,
                self.canattack, self.remaintime]


class action(object):
    def __init__(self, actions):
        self.linear_vel = actions[0]
        self.angle_vel = actions[1]
        self.fire = actions[2]