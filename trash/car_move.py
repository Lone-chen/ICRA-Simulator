 # -*- coding: cp936 -*-
import os, sys, pygame

from sys import exit
from pygame.locals import *


class car_move:
    def __init__(self, img_car, rect, speed):

        # rect �ǻ����˵�λ�ã�speed�����ƶ��ٶ�
        self.imgs = img_car.subsurface(Rect((64.5, 0), (70,70)))
        self.rect = rect
        self.speed = speed

    # �����¼���ʱ���ƶ�������
    def update(self, screen, press_keys):
        # �˳�
        if press_keys[K_ESCAPE]:
            exit()

        # ���ݰ��µķ�������ƶ�������
        if press_keys[K_LEFT]:

            self.rect.left -= self.speed
            # ����������޷����ƶ�
            if self.rect.left <= 0:
                self.rect.left = 0
            # �ж��Ƿ���ײ��70��һ���������ϰ��﷽��߳�

                        # self.rect.left += self.speed
                        # break   # ��������ײ��ԭ��������Forѭ��
            # ������������ʹ�����˲��������ƶ�ʱ�Ķ���
            screen.blit(self.imgs, self.rect)
            return 0

        if press_keys[K_RIGHT]:

            self.rect.left += self.speed
            # ����������޷����ƶ�
            if self.rect.right >= 810:
                self.rect.right = 810
            # �ж��Ƿ���ײ��70��һ���������ϰ��﷽��߳�

                        # self.rect.left -= self.speed
                        # break
            # ������������ʹ�����˲��������ƶ�ʱ�Ķ���

            screen.blit(self.imgs, self.rect)
            return 0

        if press_keys[K_UP]:

            self.rect.top -= self.speed
            # ����������޷����ƶ�
            if self.rect.top <= 0:
                self.rect.top = 0
            # �ж��Ƿ���ײ��70��һ���������ϰ��﷽��߳�

                        # self.rect.top += self.speed
                        # break
            # ������������ʹ�����˲��������ƶ�ʱ�Ķ���

            screen.blit(self.imgs, self.rect)
            return 0

        if press_keys[K_DOWN]:

            self.rect.top += self.speed
            # ����������޷����ƶ�
            if self.rect.bottom >= 510:
                self.rect.bottom = 510
            # �ж��Ƿ���ײ��70��һ���������ϰ��﷽��߳�

                        # self.rect.top -= self.speed
                        # break
            # ������������ʹ�����˲��������ƶ�ʱ�Ķ���

            screen.blit(self.imgs[3], self.rect)
            return 0

        # ���ڲ�����ֹʱ�Ķ���
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