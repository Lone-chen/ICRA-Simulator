import pygame
import math
from pygame.locals import *
from sys import exit
from car import CAR

#初始化car，后面的列表为车的初始位置
car = CAR(0, 50, 0, 0, 0, [400, 250, 445, 250, 400, 190, 445, 190])

# 加载车的模型图象，在文件夹image中
car_image = 'image/chassis_g.png'

pygame.init()

screen = pygame.display.set_mode((810, 510), 0, 32)
pygame.display.set_caption("Car_control")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.fill((127, 127, 127))
    # 加载图象
    car_module = pygame.image.load(car_image)
    screen.blit(car_module, (car.peak[0], car.peak[1]))
    # 输入当前角度
    _angle_ = int(input())
    # 计算变换的角度
    car.angle = car.change_angle(_angle_)
    # 旋转图象
    car_module = pygame.transform.rotate(car_module, car.angle)
    car.covered_area()
    # print(car.peak[0], car.peak[1], car.peak[2], car.peak[3])
    screen.fill((127, 127, 127))
    screen.blit(car_module, (car.peak[0], car.peak[1]))

    pygame.display.update()
