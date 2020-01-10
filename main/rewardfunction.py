def reward(s, s_):
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
    f_bullet = (s_.mybullet - s.mybullet) * bullet_a1

    # check
    check_a1 = 5
    if s_.isDetected == 1 and s.isDetected == 0:
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
    if s.my_forbidden == 0 and s_.my_forbidden == 1:
        f_my_forbidden = my_forbidden_a1

    # enemy_hp_addition
    if s.enemy_hp_addition == 0 and s_.enemy_hp_addition == 1:
        if s_.enemy_hp >= 500:
            f_enemy_hp_addition = 200 * enemy_hp_a1
        else:
            f_enemy_hp = 200 * enemy_hp_a2

    # enemy_bullet_addition
    enemy_bullet_addition_a1 = -100
    if s.enemy_bullet_addition == 0 and s_.enemy_bullet_addition == 1:
        f_enemy_bullet_addition = enemy_bullet_addition_a1

    return f_my_hp + f_enemy_hp + f_bullet + f_check + f_my_hp_addition + f_my_bullet_addition + \
           f_my_forbidden + f_enemy_hp_addition + f_enemy_bullet_addition