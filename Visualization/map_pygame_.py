import sys
import pygame
from pygame.locals import *
from main.map import MAP
import main.get_line
import math
from play import ver_env
import time

A = MAP()
Env = ver_env()

def check_event(Env):
    for event in pygame.event.get():
        if event.type == QUIT:  # 接收到退出事件后退出程序
            sys.exit()

        elif event.type == KEYDOWN:
            if event.key == pygame.K_RIGHT:
                Env.carA.line_speed[0] = 25
            elif event.key == pygame.K_LEFT:
                Env.carA.line_speed[0] = -25
            elif event.key == pygame.K_UP:
                Env.carA.line_speed[1] = 25
            elif event.key == pygame.K_DOWN:
                Env.carA.line_speed[1] = -25
            elif event.key == pygame.K_w:
                Env.carA.angular_speed = 10
            elif event.key == pygame.K_s:
                Env.carA.angular_speed = -10
            elif event.key == K_a:
                Env.carA.w_vel = math.pi / 2
            elif event.key == K_d:
                Env.carA.w_vel = -math.pi / 2

        elif event.type == KEYUP:
            if event.key == pygame.K_RIGHT:
                Env.carA.line_speed[0] = 0
            elif event.key == pygame.K_LEFT:
                Env.carA.line_speed[0] = 0
            elif event.key == pygame.K_UP:
                Env.carA.line_speed[1] = 0
            elif event.key == pygame.K_DOWN:
                Env.carA.line_speed[1] = 0
            elif event.key == pygame.K_w:
                Env.carA.angular_speed = 0
            elif event.key == pygame.K_s:
                Env.carA.angular_speed = 0
            elif event.key == K_a:
                Env.carA.w_vel = 0
            elif event.key == K_d:
                Env.carA.w_vel = 0


def run_game():
    pygame.init()
    SCREEN_SIZE = (1450, A.width)
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
    screen_rect = screen.get_rect()

    # 加载图像
    newimage_A = pygame.image.load('../image/gimbal_g.png')
    newgimimage_A = pygame.image.load('../image/gimbal_g.png')
    new_gimimage_A = pygame.image.load('../image/gimbal_g.png')
    gimimage_A = pygame.image.load('../image/gimbal_g.png')
    image_A = pygame.image.load('../image/chassis_g.png')
    gim_rect_A = gimimage_A.get_rect()


    newimage_B = pygame.image.load('../image/gimbal_g.png')
    newgimimage_B = pygame.image.load('../image/gimbal_g.png')
    new_gimimage_B = pygame.image.load('../image/gimbal_g.png')
    gimimage_B = pygame.image.load('../image/gimbal_g.png')
    image_B = pygame.image.load('../image/chassis_g.png')
    gim_rect_B = gimimage_B.get_rect()


    pygame.display.set_caption("map")
    R1 = pygame.image.load("../image/1.png").convert()
    R2 = pygame.image.load("../image/2.png").convert()
    F = pygame.image.load("../image/3.png").convert()
    B1 = pygame.image.load("../image/4.png").convert()
    B1_ = pygame.image.load("../image/4_.png").convert()
    B2 = pygame.image.load("../image/5.png").convert()
    B3 = pygame.image.load("../image/7.png").convert()

    # clock对象
    clock = pygame.time.Clock()

    # 字体显示
    text_surface = []
    for i in range(0, 22):
        text_surface.append(0)
    env_surface = []
    for i in range(0, 10):
        env_surface.append(0)
    font = pygame.font.SysFont("simsunnsimsun", 16)

    textA_surface = font.render("CarA : ", True, (255, 255, 255))
    textB_surface = font.render("CarB : ", True, (255, 255, 255))
    text_surface[0] = font.render("Hp : ", True, (255, 255, 255))
    text_surface[1] = font.render("Bullet : ", True, (255, 255, 255))
    text_surface[2] = font.render("Heat : ", True, (255, 255, 255))
    text_surface[3] = font.render("X : ", True, (255, 255, 255))
    text_surface[4] = font.render("Y : ", True, (255, 255, 255))
    text_surface[5] = font.render("Hest_Freeze : ", True, (255, 255, 255))
    text_surface[6] = font.render("Angle : ", True, (255, 255, 255))
    text_surface[7] = font.render("", True, (255, 255, 255))
    text_surface[8] = font.render("V_Shoot : ", True, (255, 255, 255))
    text_surface[9] = font.render("W_Gim : ", True, (255, 255, 255))
    text_surface[10] = font.render("V_x : ", True, (255, 255, 255))
    text_surface[11] = font.render("V_y : ", True, (255, 255, 255))
    text_surface[12] = font.render("Angle_V : ", True, (255, 255, 255))
    text_surface[13] = font.render("", True, (255, 255, 255))
    text_surface[14] = font.render("Gim_Angle : ", True, (255, 255, 255))
    text_surface[15] = font.render("Move_Forb : ", True, (255, 255, 255))
    text_surface[16] = font.render("Shoot_Forb : ", True, (255, 255, 255))
    text_surface[17] = font.render("IsDetected : ", True, (255, 255, 255))
    text_surface[18] = font.render("InSight : ", True, (255, 255, 255))
    text_surface[19] = font.render("HpBuff : ", True, (255, 255, 255))
    text_surface[20] = font.render("BulletBuff : ", True, (255, 255, 255))
    text_surface[21] = font.render("Meet_Barrier : ", True, (255, 255, 255))

    env_surface[0] = font.render("Enviroment : ", True, (255, 255, 255))
    env_surface[1] = font.render("Time : ", True, (255, 255, 255))
    env_surface[2] = font.render("A_HpBuff : ", True, (255, 255, 255))
    env_surface[3] = font.render("B_HpBuff : ", True, (255, 255, 255))
    env_surface[4] = font.render("A_BulletBuff : ", True, (255, 255, 255))
    env_surface[5] = font.render("B_BulletBuff : ", True, (255, 255, 255))
    env_surface[6] = font.render("MoveForb : ", True, (255, 255, 255))
    env_surface[7] = font.render("ShootForb : ", True, (255, 255, 255))
    env_surface[8] = font.render("A_Fired : ", True, (255, 255, 255))
    env_surface[9] = font.render("B_Fired : ", True, (255, 255, 255))

    while True:
        screen.fill((0, 0, 0))
        x = [820, 1040, 1260]

        rect_A = newimage_A.get_rect()
        rect_A.centerx = Env.carA.x
        rect_A.centery = Env.carA.y
        gim_rect_A.centerx = Env.carA.x
        gim_rect_A.centery = Env.carA.y


        rect_B = newimage_B.get_rect()
        rect_B.centerx = Env.carB.x
        rect_B.centery = Env.carB.y
        gim_rect_B.centerx = Env.carB.x
        gim_rect_B.centery = Env.carB.y

        time_passed = clock.tick()

        for i in range(0, A.width):
            for j in range(0,A.length):
                screen.fill((79, 79, 79), Rect(j, i, 1, 1))

        for i in range(0, A.width):
            for j in range(0,A.length):
                if A.map[i][j] == 1:
                    screen.fill((156, 156, 156), Rect(j, i, 1, 1))
                if A.map[i][j] == 8:
                    screen.fill((255, 179, 0), Rect(j, i, 1, 1))

        screen.blit(R1, A.initial_start[0])
        screen.blit(R1, A.initial_start[1])
        screen.blit(R2, A.initial_start[2])
        screen.blit(R2, A.initial_start[3])

        screen.blit(B1, A.barrier_start[0])
        screen.blit(B2, A.barrier_start[1])
        screen.blit(B1_, A.barrier_start[2])
        screen.blit(B3, A.barrier_start[3])
        screen.blit(B3, A.barrier_start[4])
        screen.blit(B1_, A.barrier_start[5])
        screen.blit(B2, A.barrier_start[6])
        screen.blit(B1, A.barrier_start[7])

        screen.blit(F, A.area_start[0])
        screen.blit(F, A.area_start[1])
        screen.blit(F, A.area_start[2])
        screen.blit(F, A.area_start[3])
        screen.blit(F, A.area_start[4])
        screen.blit(F, A.area_start[5])

        screen.blit(newimage_A, rect_A)
        screen.blit(new_gimimage_A, gim_rect_A)
        screen.blit(newimage_B, rect_B)
        screen.blit(new_gimimage_B, gim_rect_B)

        check_event(Env)

        # 更新属性
        Env.carA.angle = (Env.carA.angle + Env.carA.angular_speed) % 360
        Env.carA.pitch = (Env.carA.pitch + Env.carA.w_vel) % 360

        Env.carB.angle = (Env.carB.angle + Env.carB.angular_speed) % 360
        Env.carB.pitch = (Env.carB.pitch + Env.carB.w_vel) % 360
        Env.carB.x += Env.carB.line_speed[0] * 0.1
        Env.carB.y += Env.carB.line_speed[1] * 0.1
        # 判断A，B是否撞到障碍物或者墙壁
        if Env.carA.line_speed[0] > 0 and rect_A.right < A.length:
            Env.carA.x += Env.carA.line_speed[0] * 0.1
            if Env.carA.on_barriers() == 1:
                Env.carA.x -= Env.carA.line_speed[0] * 0.1
            rect_A.centerx = Env.carA.x
            gim_rect_A.centerx = Env.carA.x
        else:
            pass
        if Env.carA.line_speed[0] < 0 and rect_A.left > 0:
            Env.carA.x += Env.carA.line_speed[0] * 0.1
            if Env.carA.on_barriers() == 1:
                Env.carA.x -= Env.carA.line_speed[0] * 0.1
            rect_A.centerx = Env.carA.x
            gim_rect_A.centerx = Env.carA.x
        else:
            pass
        if Env.carA.line_speed[1] > 0 and rect_A.bottom < screen_rect.bottom:
            Env.carA.y += Env.carA.line_speed[1] * 0.1
            if Env.carA.on_barriers() == 1:
                Env.carA.y -= Env.carA.line_speed[1] * 0.1
            rect_A.centery = Env.carA.y
            gim_rect_A.centery = Env.carA.y
        else:
            pass
        if Env.carA.line_speed[1] < 0 and rect_A.top > screen_rect.top:
            Env.carA.y += Env.carA.line_speed[1] * 0.1
            if Env.carA.on_barriers() == 1:
                Env.carA.y -= Env.carA.line_speed[1] * 0.1
            rect_A.centery = Env.carA.y
            gim_rect_A.centery = Env.carA.y
        else:
            pass
        # print(rect_A.top, rect_A.bottom, rect_A.left, rect_A.right)
        # print(screen_rect.top, screen_rect.bottom, 0, A.length)

        if Env.carB.line_speed[0] > 0 and rect_B.right < A.length:
            Env.carB.x += Env.carB.line_speed[0] * 0.1
            if Env.carB.on_barriers() == 1:
                Env.carB.x -= Env.carB.line_speed[0] * 0.1
            rect_B.centerx = Env.carB.x
            gim_rect_B.centerx = Env.carB.x
        else:
            pass
        if Env.carB.line_speed[0] < 0 and rect_B.left > 0:
            Env.carB.x += Env.carB.line_speed[0] * 0.1
            if Env.carB.on_barriers() == 1:
                Env.carB.x -= Env.carB.line_speed[0] * 0.1
            rect_B.centerx = Env.carB.x
            gim_rect_B.centerx = Env.carB.x
        else:
            pass
        if Env.carB.line_speed[1] > 0 and rect_B.bottom < screen_rect.bottom:
            Env.carB.y += Env.carB.line_speed[1] * 0.1
            if Env.carB.on_barriers() == 1:
                Env.carB.y -= Env.carB.line_speed[1] * 0.1
            rect_B.centery = Env.carB.y
            gim_rect_B.centery = Env.carB.y
        else:
            pass
        if Env.carB.line_speed[1] < 0 and rect_B.top > screen_rect.top:
            Env.carB += Env.carB.line_speed[1] * 0.1
            if Env.carB.on_barriers() == 1:
                Env.carB.y -= Env.carB.line_speed[1] * 0.1
            rect_B.centery = Env.carB.y
            gim_rect_A.centery = Env.carA.y
        else:
            pass

        # 更新图像
        newimage_A = pygame.transform.rotate(image_A, Env.carA.angle)
        rect_A = newimage_A.get_rect(center=rect_A.center)
        newgimimage_A = pygame.transform.rotate(gimimage_A, Env.carA.angle)
        gim_rect_A = newgimimage_A.get_rect(center=gim_rect_A.center)
        new_gimimage_A = pygame.transform.rotate(newgimimage_A, Env.carA.pitch)
        gim_rect_A = new_gimimage_A.get_rect(center=gim_rect_A.center)

        newimage_B = pygame.transform.rotate(image_B, Env.carB.angle)
        rect_B = newimage_B.get_rect(center=rect_B.center)
        newgimimage_B = pygame.transform.rotate(gimimage_B, Env.carB.angle)
        gim_rect_B = newgimimage_B.get_rect(center=gim_rect_B.center)
        new_gimimage_B = pygame.transform.rotate(newgimimage_B, Env.carB.pitch)
        gim_rect_B = new_gimimage_B.get_rect(center=gim_rect_B.center)

        screen.blit(textA_surface, (x[0], 20))
        for i in range(0, 22):
            screen.blit(text_surface[i], (x[0] + 45, 20 + i*18))
        screen.blit(textB_surface, (x[1], 20))
        for i in range(0, 22):
            screen.blit(text_surface[i], (x[1] + 45, 20 + i*18))
        screen.blit(env_surface[0], (x[2], 20))
        for i in range(1, 10):
            screen.blit(env_surface[i], (x[2] + 45, 20 + i * 18))

        text_surfaceA = []
        for i in range(0, 22):
            text_surfaceA.append(0)

        text_surfaceB = []
        for i in range(0, 22):
            text_surfaceB.append(0)

        text_enviroment = []
        for i in range(0, 10):
            text_enviroment.append(0)

        text_surfaceA[0] = font.render(str(Env.carA.hp), True, (255, 255, 255))
        text_surfaceA[1] = font.render(str(Env.carA.bullet), True, (255, 255, 255))
        text_surfaceA[2] = font.render(str(Env.carA.heat), True, (255, 255, 255))
        text_surfaceA[3] = font.render(str(round(Env.carA.x, 2)), True, (255, 255, 255))
        text_surfaceA[4] = font.render(str(round(Env.carA.y, 2)), True, (255, 255, 255))
        text_surfaceA[5] = font.render(str(Env.carA.HEAT_FREEZE), True, (255, 255, 255))
        text_surfaceA[6] = font.render(str(round(Env.carA.angle, 2)), True, (255, 255, 255))
        text_surfaceA[7] = font.render("", True, (255, 255, 255))
        text_surfaceA[8] = font.render(str(round(Env.carA.v, 2)), True, (255, 255, 255))
        text_surfaceA[9] = font.render(str(round(Env.carA.w_vel, 2)), True, (255, 255, 255))
        text_surfaceA[10] = font.render(str(round(Env.carA.line_speed[0], 2)), True, (255, 255, 255))
        text_surfaceA[11] = font.render(str(round(Env.carA.line_speed[1], 2)), True, (255, 255, 255))
        text_surfaceA[12] = font.render(str(round(Env.carA.angular_speed, 2)), True, (255, 255, 255))
        text_surfaceA[13] = font.render("", True, (255, 255, 255))
        text_surfaceA[14] = font.render(str(round(Env.carA.pitch, 2)), True, (255, 255, 255))
        text_surfaceA[15] = font.render(str(Env.carA.move_forbiden), True, (255, 255, 255))
        text_surfaceA[16] = font.render(str(Env.carA.shoot_forbiden), True, (255, 255, 255))
        text_surfaceA[17] = font.render(str(Env.carA.isdetected), True, (255, 255, 255))
        text_surfaceA[18] = font.render(str(Env.carA.on_buff()), True, (255, 255, 255))
        text_surfaceA[19] = font.render(str(Env.carA.hpbuff), True, (255, 255, 255))
        text_surfaceA[20] = font.render(str(Env.carA.bulletbuff), True, (255, 255, 255))
        text_surfaceA[21] = font.render(str(Env.carA.on_barriers()), True, (255, 255, 255))

        text_surfaceB[0] = font.render(str(Env.carB.hp), True, (255, 255, 255))
        text_surfaceB[1] = font.render(str(Env.carB.bullet), True, (255, 255, 255))
        text_surfaceB[2] = font.render(str(Env.carB.heat), True, (255, 255, 255))
        text_surfaceB[3] = font.render(str(Env.carB.x), True, (255, 255, 255))
        text_surfaceB[4] = font.render(str(Env.carB.y), True, (255, 255, 255))
        text_surfaceB[5] = font.render(str(Env.carB.HEAT_FREEZE), True, (255, 255, 255))
        text_surfaceB[6] = font.render(str(round(Env.carB.angle, 2)), True, (255, 255, 255))
        text_surfaceB[7] = font.render("", True, (255, 255, 255))
        text_surfaceB[8] = font.render(str(round(Env.carB.v, 2)), True, (255, 255, 255))
        text_surfaceB[9] = font.render(str(round(Env.carB.w_vel, 2)), True, (255, 255, 255))
        text_surfaceB[10] = font.render(str(round(Env.carB.line_speed[0], 2)), True, (255, 255, 255))
        text_surfaceB[11] = font.render(str(round(Env.carB.line_speed[1], 2)), True, (255, 255, 255))
        text_surfaceB[12] = font.render(str(round(Env.carB.angular_speed, 2)), True, (255, 255, 255))
        text_surfaceB[13] = font.render("", True, (255, 255, 255))
        text_surfaceB[14] = font.render(str(round(Env.carB.pitch, 2)), True, (255, 255, 255))
        text_surfaceB[15] = font.render(str(Env.carB.move_forbiden), True, (255, 255, 255))
        text_surfaceB[16] = font.render(str(Env.carB.shoot_forbiden), True, (255, 255, 255))
        text_surfaceB[17] = font.render(str(Env.carB.isdetected), True, (255, 255, 255))
        text_surfaceB[18] = font.render(str(Env.carB.on_buff()), True, (255, 255, 255))
        text_surfaceB[19] = font.render(str(Env.carB.hpbuff), True, (255, 255, 255))
        text_surfaceB[20] = font.render(str(Env.carB.bulletbuff), True, (255, 255, 255))
        text_surfaceB[21] = font.render(str(Env.carB.on_barriers()), True, (255, 255, 255))

        text_enviroment[1] = font.render(str(Env.time / 10), True, (255, 255, 255))
        text_enviroment[2] = font.render(str(Env.chufa[0]), True, (255, 255, 255))
        text_enviroment[3] = font.render(str(Env.chufa[1]), True, (255, 255, 255))
        text_enviroment[4] = font.render(str(Env.chufa[2]), True, (255, 255, 255))
        text_enviroment[5] = font.render(str(Env.chufa[3]), True, (255, 255, 255))
        text_enviroment[6] = font.render(str(Env.chufa[4]), True, (255, 255, 255))
        text_enviroment[7] = font.render(str(Env.chufa[5]), True, (255, 255, 255))
        text_enviroment[8] = font.render(str(Env.Afire), True, (255, 255, 255))
        text_enviroment[9] = font.render(str(Env.Bfire), True, (255, 255, 255))

        for i in range(0, 22):
            screen.blit(text_surfaceA[i], (x[0] + 145, 20 + i * 18))
        for i in range(0, 22):
            screen.blit(text_surfaceB[i], (x[1] + 145, 20 + i * 18))
        for i in range(1, 10):
            screen.blit(text_enviroment[i], (x[2] + 145, 20 + i * 18))

        pygame.display.update()


print(A.areas)
run_game()