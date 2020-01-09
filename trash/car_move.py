 # -*- coding: cp936 -*-
import os, sys, pygame

from sys import exit
from pygame.locals import *


class car_move:
    def __init__(self, img_car, rect, speed):

        # rect 是机器人的位置，speed则是移动速度
        self.imgs = img_car.subsurface(Rect((64.5, 0), (70,70)))
        self.rect = rect
        self.speed = speed

    # 当按下键盘时，移动机器人
    def update(self, screen, press_keys):
        # 退出
        if press_keys[K_ESCAPE]:
            exit()

        # 根据按下的方向键来移动机器人
        if press_keys[K_LEFT]:

            self.rect.left -= self.speed
            # 如果碰壁则无法再移动
            if self.rect.left <= 0:
                self.rect.left = 0
            # 判断是否碰撞，70是一个基数是障碍物方块边长

                        # self.rect.left += self.speed
                        # break   # 发生了碰撞则复原并跳出此For循环
            # 接下来的用于使机器人产生向右移动时的动画
            screen.blit(self.imgs, self.rect)
            return 0

        if press_keys[K_RIGHT]:

            self.rect.left += self.speed
            # 如果碰壁则无法再移动
            if self.rect.right >= 810:
                self.rect.right = 810
            # 判断是否碰撞，70是一个基数是障碍物方块边长

                        # self.rect.left -= self.speed
                        # break
            # 接下来的用于使机器人产生向右移动时的动画

            screen.blit(self.imgs, self.rect)
            return 0

        if press_keys[K_UP]:

            self.rect.top -= self.speed
            # 如果碰壁则无法再移动
            if self.rect.top <= 0:
                self.rect.top = 0
            # 判断是否碰撞，70是一个基数是障碍物方块边长

                        # self.rect.top += self.speed
                        # break
            # 接下来的用于使机器人产生向上移动时的动画

            screen.blit(self.imgs, self.rect)
            return 0

        if press_keys[K_DOWN]:

            self.rect.top += self.speed
            # 如果碰壁则无法再移动
            if self.rect.bottom >= 510:
                self.rect.bottom = 510
            # 判断是否碰撞，70是一个基数是障碍物方块边长

                        # self.rect.top -= self.speed
                        # break
            # 接下来的用于使机器人产生向下移动时的动画

            screen.blit(self.imgs[3], self.rect)
            return 0

        # 用于产生静止时的动画
        screen.blit(self.imgs, self.rect)

        return 0


if __name__ == "__main__":
    speed_car = 20
    dwTime = 6
    r_car = Rect(0, 0, 70, 70)
    pygame.init()
    clock = pygame.time.Clock()
    carr = pygame.image.load('../image/chassis_g.png').convert_alpha()
    Andr = car_move(carr, r_car, speed_car)