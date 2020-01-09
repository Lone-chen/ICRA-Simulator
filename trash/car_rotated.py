import pygame
import math
from pygame.locals import *
from sys import exit
from main.car import CAR

# 初始化car，后面的列表为车的初始位置
car = CAR(0, 50, 0,  0, [400, 250, 445, 250, 400, 190, 445, 190])
print(car.peak)
# 加载车的模型图象，在文件夹image中
chassis_image = 'image/chassis_g.png'
# gimbal_image = 'image/gimbal_g.png'

pygame.init()

screen = pygame.display.set_mode((810, 510), 0, 32)
pygame.display.set_caption("Car_control")
_angle_ = 0
_angle_a = 0

chassis_module = pygame.image.load(chassis_image)
chassisRect = chassis_module.get_rect()
chassisRect = chassisRect.move((810 - chassisRect.width) / 2, (510 - chassisRect.height) / 2)
screen.blit(chassis_module, chassisRect)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                _angle_ = -math.radians(1) % 360
            if event.key == K_LEFT:
                _angle_ = math.radians(1) % 360
            if event.key == K_UP:
                _angle_a = (_angle_a + math.radians(1) % 360)
            if event.key == K_DOWN:
                _angle_a = (_angle_a - math.radians(1) % 360)
        if event.type == KEYUP:
            _angle_ = 0

    screen.fill((127, 127, 127))
    # 计算变换的角度
    car.angle = car.change_angle((_angle_ + _angle_a) % 360)
    # 旋转图象
    new_chassis_module = pygame.transform.rotate(chassis_module, car.angle)
    newRect = new_chassis_module.get_rect(center=chassisRect.center)
    car.covered_area()

    screen.fill((127, 127, 127))
    screen.blit(new_chassis_module, newRect)
    pygame.display.update()
