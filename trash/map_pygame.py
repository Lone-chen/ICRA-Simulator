import sys
import py
import main.map
import main.get_line
import math

A = main.map.MAP()

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
        self.newimage = pygame.image.load('image/gimbal_g.png')
        self.newgimimage = pygame.image.load('image/gimbal_g.png')
        self.new_gimimage = pygame.image.load('image/gimbal_g.png')
        self.gimimage = pygame.image.load('image/gimbal_g.png')
        self.image = pygame.image.load('image/chassis_g.png')
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
                list = get_line.get_lines(int(self.x[i]), int(self.y[i]), int(self.x[j]), int(self.y[j]))
                for p, q in list:
                    if p>0 and p<810 and q>0 and q<510 and A.map[q][p] == 1:
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
    SCREEN_SIZE = (810, 510)
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
    pygame.display.set_caption("map")
    R1 = pygame.image.load("image/1.png").convert()
    R2 = pygame.image.load("image/2.png").convert()
    F = pygame.image.load("image/3.png").convert()
    B1 = pygame.image.load("image/4.png").convert()
    B1_ = pygame.image.load("image/4_.png").convert()
    B2 = pygame.image.load("image/5.png").convert()
    B3 = pygame.image.load("image/7.png").convert()
    # clock对象
    clock = pygame.time.Clock()
    car = Ship(screen)
    # 字体显示
    font = pygame.font.SysFont("simsunnsimsun", 16)
    text1_surface = font.render("V_x : ", True, (255, 255, 255))
    text3_surface = font.render("V_y : ", True, (255, 255, 255))
    text5_surface = font.render("X  : ", True, (255, 255, 255))
    text7_surface = font.render("Y  : ", True, (255, 255, 255))
    text9_surface = font.render("judge: ", True, (255, 255, 255))
    text11_surface = font.render("angle: ", True, (255, 255, 255))
    text13_surface = font.render("  gim_angle: ", True, (255, 255, 255))

    while True:
        screen.fill((110, 123, 139))

        time_passed = clock.tick()

        for i in range(0, 510):
            for j in range(0, 810):
                if A.map[i][j] == 1:
                    screen.fill((133, 106, 106), Rect(j, i, 1, 1))
                if A.map[i][j] == 8:
                    screen.fill((230, 213, 87), Rect(j, i, 1, 1))

        screen.blit(R1, (0, 0))
        screen.blit(R1, (0, 410))
        screen.blit(R2, (710, 410))
        screen.blit(R2, (710, 0))

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

        car.blitme()

        check_event(car)
        car.update()

        screen.blit(text1_surface, (150, 20))
        screen.blit(text3_surface, (150, 38))
        screen.blit(text5_surface, (150, 56))
        screen.blit(text7_surface, (150, 74))
        screen.blit(text9_surface, (150, 92))
        screen.blit(text11_surface, (150, 110))
        screen.blit(text13_surface, (110, 128))
        text2_surface = font.render(str(car.acel_right), True, (255, 255, 255))
        text4_surface = font.render(str(car.acel_up), True, (255, 255, 255))
        text6_surface = font.render(str(car.rect.centerx), True, (255, 255, 255))
        text8_surface = font.render(str(car.rect.centery), True, (255, 255, 255))
        text10_surface = font.render(str(car.barrairs), True, (255, 255, 255))
        text12_surface = font.render(str(round(car.angle, 2)), True, (255, 255, 255))
        text14_surface = font.render(str(round(car.gimangle, 2)), True, (255, 255, 255))
        screen.blit(text2_surface, (198, 20))
        screen.blit(text4_surface, (198, 38))
        screen.blit(text6_surface, (198, 56))
        screen.blit(text8_surface, (198, 74))
        screen.blit(text10_surface, (207, 92))
        screen.blit(text12_surface, (207, 110))
        screen.blit(text14_surface, (207, 128))

        pygame.display.update()

run_game()


