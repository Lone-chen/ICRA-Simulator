from car import CAR

car1 = CAR()
car2 = CAR()


class state(object):
    object.myhp = car1.hp
    object.mybullet = car1.bullet
    object.mtheat = car1.heat
    object.fired = 0  # 0为未开火，1为开火
    object.mypitch = car1.pitch
    object.mydebuff = 0
    object.my_x = car1.x
    object.my_y = car1.y
    object.theta = 0
    object.linear_val = 0
    object.angle_val = 0

    object.enemyhp = car2.hp
    object.enemybullet = car2.bullet
    object.enemyheat = car2.heat
    object.enemypitch = car2.pitch
    object.enemydebuff = 0
    object.enemy_x = car2.x
    object.enemy_y = car2.y
    object.isDetected = 0  # 0为未被侦测，1为被侦测

    object.time = 180


class action(object):

