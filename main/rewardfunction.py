def reward(s, s_, id):
    my_forbidden = s.chufa[4] + s.chufa[5]
    my_forbidden_ = s_.chufa[4] + s_.chufa[5]
    if id == 0:
        enemy_hp_addition = s.chufa[1]
        enemy_hp_addition_ = s_.chufa[1]
        enemy_bullet_addition = s.chufa[3]
        enemy_bullet_addition_ = s_.chufa[3]
    else:
        enemy_hp_addition = s.chufa[0]
        enemy_hp_addition_ = s_.chufa[0]
        enemy_bullet_addition = s.chufa[4]
        enemy_bullet_addition_ = s_.chufa[4]

    # my_hp
    my_hp_a1 = 10
    my_hp_a2 = 18
    if s_.myhp >= 500:
        f_my_hp = (s_.myhp-s.myhp) * my_hp_a1
    else:
        f_my_hp = (s_.myhp-s.myhp) * my_hp_a2

    # enemy_hp
    enemy_hp_a1 = 15
    enemy_hp_a2 = 20
    if s_.enemy_hp >= 500:
        f_enemy_hp = -1 * (s_.enemyhp - s.myhp) * enemy_hp_a1
    else:
        f_enemy_hp = -1 * (s_.enemyhp - s.myhp) * enemy_hp_a2

    # bullet
    bullet_a1 = 10
    f_bullet = -1 * (s_.mybullet - s.mybullet) * bullet_a1

    # check
    check_a1 = 20
    if s_.canattack == 1 and s.canattack == 0:
        f_check = check_a1
    else:
        f_check = 0

    # my_hp_addition
    my_hp_addition_a1 = 200
    if s_.time % 60 >= 20 and s.my_hp_addition == 0 and s_.my_hp_addition == 1:
        f_my_hp_addition = my_hp_addition_a1
    else:
        f_my_hp_addition = 0

    # my_bullet_addition
    my_bullet_addition_a1 = 200
    if s.my_bullet_addition == 0 and s_.my_bullet_addition == 1:
        f_my_bullet_addition = my_bullet_addition_a1
    else:
        f_my_bullet_addition = 0

    # my_forbidden
    my_forbidden_a1 = -200
    if my_forbidden == 0 and my_forbidden_ == 1:
        f_my_forbidden = my_forbidden_a1
    else:
        f_my_forbidden = 0


    # enemy_hp_addition
    if enemy_hp_addition == 0 and enemy_hp_addition_ == 1:
        if s_.enemy_hp >= 500:
            f_enemy_hp_addition = 200 * enemy_hp_a1
        else:
            f_enemy_hp_addition = 200 * enemy_hp_a2
    else:
        f_enemy_hp_addition = 0

    # enemy_bullet_addition
    enemy_bullet_addition_a1 = -100
    if enemy_bullet_addition == 0 and enemy_bullet_addition_ == 1:
        f_enemy_bullet_addition = enemy_bullet_addition_a1
    else:
        f_enemy_bullet_addition = 0

    return f_my_hp + f_enemy_hp + f_bullet + f_check + f_my_hp_addition + f_my_bullet_addition + \
           f_my_forbidden + f_enemy_hp_addition + f_enemy_bullet_addition