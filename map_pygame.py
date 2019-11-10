import os, sys, pygame
from pygame.locals import *
from sys import exit
import map
import visual_field
import get_line

A = map.MAP()

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x_car = int(input())
y_car = int(input())

list1 = get_line.get_lines(x1, y1, x_car, y_car)
list2 = get_line.get_lines(x2, y2, x_car, y_car)

# 初始化pygame，为使用硬件做准备
pygame.init()
# 创建了一个窗口
SCREEN_SIZE = (1620, 1020)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
# 设置窗口标题
pygame.display.set_caption("map")

while True:
    screen.fill((110, 123, 139))

    for i in range(0, 5100):
        for j in range(0, 8100):
            if A.map[i][j] == 1:
                screen.fill((16, 78, 139), Rect(j // 5, i // 5, 1, 1))
                # 如果为障碍物，像素块显示为深蓝

            if A.map[i][j] == 2:
                screen.fill((255, 181, 197), Rect(j // 5, i // 5, 1, 1))
                # 如果为红方回血区，像素块显示为浅红

            if A.map[i][j] == 3:
                screen.fill((187, 255, 255), Rect(j // 5, i // 5, 1, 1))
                # 如果为蓝方回血区，像素块显示为浅蓝

            if A.map[i][j] == 4:
                screen.fill((205, 85, 85), Rect(j // 5, i // 5, 1, 1))
                # 如果为红方弹药补给区，像素块显示为红

            if A.map[i][j] == 5:
                screen.fill((24, 116, 205), Rect(j // 5, i // 5, 1, 1))
                # 如果为蓝方弹药补给区，像素块显示为蓝

            if A.map[i][j] == 6:
                screen.fill((139, 137, 137), Rect(j // 5, i // 5, 1, 1))
                # 如果为禁止射击区，像素块显示为灰色

            if A.map[i][j] == 7:
                screen.fill((28, 28, 28), Rect(j // 5, i // 5, 1, 1))
                # 如果为禁止移动区，像素块显示为黑色

    for i, j in list1:
        screen.fill((255, 255, 255), Rect(i * 2, j * 2, 1, 1))

    for i, j in list2:
        screen.fill((255, 255, 255), Rect(i * 2, j * 2, 1, 1))

    for event in pygame.event.get():
        if event.type == QUIT:  # 接收到退出事件后退出程序
            exit()

    pygame.display.update()
