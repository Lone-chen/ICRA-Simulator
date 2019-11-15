 # -*- coding: cp936 -*-
import os, sys, pygame

from sys import exit
from pygame.locals import *


class car_move:
    def __init__(self, img, rect, speed):

        # full_img 是整张图
        # rect 是机器人的位置，speed则是移动速度
        self.ful_img = img
        self.rect = rect
        self.speed = speed
        self.num = 0

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
            for n in range(len(block_group)-1):     # block_group列表记录所有的方块，最后一位记录终点方块，判断胜利调用最后一位，除此之外不涉及最后一位
                # 此后两个if判断与某一方块是否碰撞
                if self.rect.top > block_group[n].rect.top - 70 and self.rect.bottom < block_group[n].rect.bottom + 70:
                    if self.rect.right > block_group[n].rect.right > self.rect.left:
                        self.rect.left += self.speed
                        break   # 发生了碰撞则复原并跳出此For循环
            # 接下来的if...else用于使机器人产生向左移动时的动画
            if self.num % 3 == 1 or self.num % 3 == 0:
                screen.blit(self.imgs[2], self.rect)
                return 0
            else:
                screen.blit(self.imgs[0], self.rect)
                return 0

        if press_keys[K_RIGHT]:

            self.rect.left += self.speed
            # 如果碰壁则无法再移动
            if self.rect.right >= 810:
                self.rect.right = 810
            # 判断是否碰撞，70是一个基数是障碍物方块边长
            for n in range(len(block_group)-1):
                if self.rect.top > block_group[n].rect.top - 70 and self.rect.bottom < block_group[n].rect.bottom + 70:
                    if self.rect.left < block_group[n].rect.left < self.rect.right:
                        self.rect.left -= self.speed
                        break
            # 接下来的if...else用于使机器人产生向右移动时的动画
            if self.num % 3 == 1 or self.num % 3 == 0:
                screen.blit(self.imgs[1], self.rect)
                return 0
            else:
                screen.blit(self.imgs[0], self.rect)
                return 0

        if press_keys[K_UP]:

            self.rect.top -= self.speed
            # 如果碰壁则无法再移动
            if self.rect.top <= 0:
                self.rect.top = 0
            # 判断是否碰撞，70是一个基数是障碍物方块边长
            for n in range(len(block_group)-1):
                if self.rect.left > block_group[n].rect.left - 70 and self.rect.right < block_group[n].rect.right + 70:
                    if self.rect.bottom > block_group[n].rect.bottom > self.rect.top:
                        self.rect.top += self.speed
                        break
            # 接下来的if...else用于使机器人产生向上移动时的动画
            if self.num % 3 == 1 or self.num % 3 == 0:
                screen.blit(self.imgs[9], self.rect)
                return 0
            else:
                screen.blit(self.imgs[0], self.rect)
                return 0

        if press_keys[K_DOWN]:

            self.rect.top += self.speed
            # 如果碰壁则无法再移动
            if self.rect.bottom >= 510:
                self.rect.bottom = 510
            # 判断是否碰撞，70是一个基数是障碍物方块边长
            for n in range(len(block_group)-1):
                if self.rect.left > block_group[n].rect.left - 70 and self.rect.right < block_group[n].rect.right + 70:
                    if self.rect.top < block_group[n].rect.top < self.rect.bottom:
                        self.rect.top -= self.speed
                        break
            # 接下来的if...else用于使机器人产生向下移动时的动画
            if self.num % 3 == 1 or self.num % 3 == 0:
                screen.blit(self.imgs[3], self.rect)
                return 0
            else:
                screen.blit(self.imgs[0], self.rect)
                return 0

        # 用于产生静止时的动画
        if 3 >= self.num >= 0 or self.num > 7:
            screen.blit(self.imgs[0], self.rect)
        elif self.num == 5 or self.num == 4:
            screen.blit(self.imgs[5], self.rect)
        elif self.num == 6 or self.num == 7:
            screen.blit(self.imgs[6], self.rect)

        return 0


class Block:
    def __init__(self, img, rect):
        self.img = img
        self.rect = rect