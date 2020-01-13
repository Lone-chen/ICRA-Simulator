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

class Ship():
    def __init__(self, screen):
        """初始化"""
        self.begin_angle1 = math.atan(2/3)
        self.begin_angle2 = math.atan(3/2)
        self.screen = screen
        self.x = [0, 0, 0, 0]
        self.y = [0, 0, 0, 0]
        self.l = math.sqrt(20*20 + 30*30)
        # 加载图像
        self.newimage = pygame.image.load('../image/gimbal_g.png')
        self.newgimimage = pygame.image.load('../image/gimbal_g.png')
        self.new_gimimage = pygame.image.load('../image/gimbal_g.png')
        self.gimimage = pygame.image.load('../image/gimbal_g.png')
        self.image = pygame.image.load('../image/chassis_g.png')
        self.gim_rect = self.gimimage.get_rect()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 初始位置
        self.rect.centerx = 600
        self.rect.centery = 450
        self.gim_rect.centerx = 600
        self.gim_rect.centery = 450
        # 移动控制
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        # 加速度控制
        self.acel_right = 0
        self.acel_left = 0
        self.acel_up = 0
        self.acel_down = 0
        # 障碍物碰撞控制
        self.barrairs = True
        # 加速度控制
        self.angle = 0
        self.gimangle = 0
        self._angle_a = 0
        self.gim_angle_a = 0

    def judeg(self):
        self.barrairs = True
        self.x[0] = self.rect.centerx - math.sin(self.begin_angle1 - self.angle) * self.l
        self.y[0] = self.rect.centery - math.cos(self.begin_angle1 - self.angle) * self.l
        self.x[1] = self.rect.centerx + math.cos(self.begin_angle2 - self.angle) * self.l
        self.y[1] = self.rect.centery - math.sin(self.begin_angle2 - self.angle) * self.l
        self.x[2] = self.rect.centerx + math.sin(self.begin_angle1 - self.angle) * self.l
        self.y[2] = self.rect.centery + math.cos(self.begin_angle1 - self.angle) * self.l
        self.x[3] = self.rect.centerx - math.cos(self.begin_angle2 - self.angle) * self.l
        self.y[3] = self.rect.centery + math.sin(self.begin_angle2 - self.angle) * self.l
        for i in range(0, 4):
            for j in range(i + 1, 4):
                list = main.get_line.get_lines(int(self.x[i]), int(self.y[i]), int(self.x[j]), int(self.y[j]))
                for p, q in list:
                    if (p>0 and p<A.length and q>0 and q<A.width and A.map[q][p] == 1) or p >= A.length:
                        self.barrairs = False
        return self.barrairs

    def update(self):
        self.angle += self._angle_a
        self.gimangle += self.gim_angle_a
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.acel_right
            self.gim_rect.centerx += self.acel_right
            if self.judeg() == False:
                self.rect.centerx -= self.acel_right
                self.gim_rect.centerx -= self.acel_right
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= self.acel_right
            self.gim_rect.centerx -= self.acel_right
            if self.judeg() == False:
                self.rect.centerx += self.acel_right
                self.gim_rect.centerx += self.acel_right
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.acel_up
            self.gim_rect.centery += self.acel_up
            if self.judeg() == False:
                self.rect.centery -= self.acel_up
                self.gim_rect.centery -= self.acel_up
        if self.moving_up and self.rect.top > self.screen_rect.top and self.barrairs:
            self.rect.centery -= self.acel_up
            self.gim_rect.centery -= self.acel_up
            if self.judeg() == False:
                self.rect.centery += self.acel_up
                self.gim_rect.centery += self.acel_up
        self.newimage = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.newimage.get_rect(center=self.rect.center)
        self.newgimimage = pygame.transform.rotate(self.gimimage, self.angle)
        self.gim_rect = self.newgimimage.get_rect(center=self.gim_rect.center)
        self.new_gimimage = pygame.transform.rotate(self.newgimimage, self.gimangle)
        self.gim_rect = self.new_gimimage.get_rect(center=self.gim_rect.center)

    def blitme(self):
        self.screen.blit(self.newimage, self.rect)
        self.screen.blit(self.new_gimimage, self.gim_rect)


def check_event(ship):
    for event in pygame.event.get():
        if event.type == QUIT:  # 接收到退出事件后退出程序
            sys.exit()

        elif event.type == KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
            elif event.key == pygame.K_UP:
                ship.moving_up = True
            elif event.key == pygame.K_DOWN:
                ship.moving_down = True
            elif event.key == pygame.K_w:
                ship.acel_up += 1
            elif event.key == pygame.K_s:
                ship.acel_up -= 1
            elif event.key == pygame.K_a:
                ship.acel_right -= 1
            elif event.key == pygame.K_d:
                ship.acel_right += 1
            elif event.key == K_h:
                ship.gim_angle_a = ship.gim_angle_a - math.radians(100)
            elif event.key == K_f:
                ship.gim_angle_a = ship.gim_angle_a + math.radians(100)
            elif event.key == K_t:
                ship._angle_a = ship._angle_a + math.radians(100)
            elif event.key == K_g:
                ship._angle_a = ship._angle_a - math.radians(100)

        elif event.type == KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
            elif event.key == pygame.K_UP:
                ship.moving_up = False
            elif event.key == pygame.K_DOWN:
                ship.moving_down = False
            ship._angle_ = 0


def run_game():
    pygame.init()
    SCREEN_SIZE = (1450, A.width)
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
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
    car1 = Ship(screen)
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

        car1.blitme()

        check_event(car1)
        car1.update()

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
        text_surfaceA[3] = font.render(str(Env.carA.x), True, (255, 255, 255))
        text_surfaceA[4] = font.render(str(Env.carA.y), True, (255, 255, 255))
        text_surfaceA[5] = font.render(str(Env.carA.HEAT_FREEZE), True, (255, 255, 255))
        text_surfaceA[6] = font.render(str(round(Env.carA.angle, 2)), True, (255, 255, 255))
        text_surfaceA[7] = font.render("", True, (255, 255, 255))
        text_surfaceA[8] = font.render(str(Env.carA.v), True, (255, 255, 255))
        text_surfaceA[9] = font.render(str(round(Env.carA.w_vel, 2)), True, (255, 255, 255))
        text_surfaceA[10] = font.render(str(Env.carA.line_speed[0]), True, (255, 255, 255))
        text_surfaceA[11] = font.render(str(Env.carA.line_speed[1]), True, (255, 255, 255))
        text_surfaceA[12] = font.render(str(Env.carA.angular_speed), True, (255, 255, 255))
        text_surfaceA[13] = font.render("", True, (255, 255, 255))
        text_surfaceA[14] = font.render(str(Env.carA.pitch), True, (255, 255, 255))
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
        text_surfaceB[8] = font.render(str(Env.carB.v), True, (255, 255, 255))
        text_surfaceB[9] = font.render(str(round(Env.carB.w_vel, 2)), True, (255, 255, 255))
        text_surfaceB[10] = font.render(str(Env.carB.line_speed[0]), True, (255, 255, 255))
        text_surfaceB[11] = font.render(str(Env.carB.line_speed[1]), True, (255, 255, 255))
        text_surfaceB[12] = font.render(str(Env.carB.angular_speed), True, (255, 255, 255))
        text_surfaceB[13] = font.render("", True, (255, 255, 255))
        text_surfaceB[14] = font.render(str(Env.carB.pitch), True, (255, 255, 255))
        text_surfaceB[15] = font.render(str(Env.carB.move_forbiden), True, (255, 255, 255))
        text_surfaceB[16] = font.render(str(Env.carB.shoot_forbiden), True, (255, 255, 255))
        text_surfaceB[17] = font.render(str(Env.carB.isdetected), True, (255, 255, 255))
        text_surfaceB[18] = font.render(str(Env.carB.on_buff()), True, (255, 255, 255))
        text_surfaceB[19] = font.render(str(Env.carB.hpbuff), True, (255, 255, 255))
        text_surfaceB[20] = font.render(str(Env.carB.bulletbuff), True, (255, 255, 255))
        text_surfaceB[21] = font.render(str(Env.carB.on_barriers()), True, (255, 255, 255))

        text_enviroment[1] = font.render(str(Env.time / 10), True, (255, 255, 255))
        text_enviroment[2] = font.render(str(Env.chufa[2]), True, (255, 255, 255))
        text_enviroment[3] = font.render(str(Env.chufa[3]), True, (255, 255, 255))
        text_enviroment[4] = font.render(str(Env.chufa[4]), True, (255, 255, 255))
        text_enviroment[5] = font.render(str(Env.chufa[5]), True, (255, 255, 255))
        text_enviroment[6] = font.render(str(Env.chufa[6]), True, (255, 255, 255))
        text_enviroment[7] = font.render(str(Env.chufa[7]), True, (255, 255, 255))
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


