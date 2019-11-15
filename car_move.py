 # -*- coding: cp936 -*-
import os, sys, pygame

from sys import exit
from pygame.locals import *


class car_move:
    def __init__(self, img, rect, speed):

        # full_img ������ͼ
        # rect �ǻ����˵�λ�ã�speed�����ƶ��ٶ�
        self.ful_img = img
        self.rect = rect
        self.speed = speed
        self.num = 0

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
            for n in range(len(block_group)-1):     # block_group�б��¼���еķ��飬���һλ��¼�յ㷽�飬�ж�ʤ���������һλ������֮�ⲻ�漰���һλ
                # �˺�����if�ж���ĳһ�����Ƿ���ײ
                if self.rect.top > block_group[n].rect.top - 70 and self.rect.bottom < block_group[n].rect.bottom + 70:
                    if self.rect.right > block_group[n].rect.right > self.rect.left:
                        self.rect.left += self.speed
                        break   # ��������ײ��ԭ��������Forѭ��
            # ��������if...else����ʹ�����˲��������ƶ�ʱ�Ķ���
            if self.num % 3 == 1 or self.num % 3 == 0:
                screen.blit(self.imgs[2], self.rect)
                return 0
            else:
                screen.blit(self.imgs[0], self.rect)
                return 0

        if press_keys[K_RIGHT]:

            self.rect.left += self.speed
            # ����������޷����ƶ�
            if self.rect.right >= 810:
                self.rect.right = 810
            # �ж��Ƿ���ײ��70��һ���������ϰ��﷽��߳�
            for n in range(len(block_group)-1):
                if self.rect.top > block_group[n].rect.top - 70 and self.rect.bottom < block_group[n].rect.bottom + 70:
                    if self.rect.left < block_group[n].rect.left < self.rect.right:
                        self.rect.left -= self.speed
                        break
            # ��������if...else����ʹ�����˲��������ƶ�ʱ�Ķ���
            if self.num % 3 == 1 or self.num % 3 == 0:
                screen.blit(self.imgs[1], self.rect)
                return 0
            else:
                screen.blit(self.imgs[0], self.rect)
                return 0

        if press_keys[K_UP]:

            self.rect.top -= self.speed
            # ����������޷����ƶ�
            if self.rect.top <= 0:
                self.rect.top = 0
            # �ж��Ƿ���ײ��70��һ���������ϰ��﷽��߳�
            for n in range(len(block_group)-1):
                if self.rect.left > block_group[n].rect.left - 70 and self.rect.right < block_group[n].rect.right + 70:
                    if self.rect.bottom > block_group[n].rect.bottom > self.rect.top:
                        self.rect.top += self.speed
                        break
            # ��������if...else����ʹ�����˲��������ƶ�ʱ�Ķ���
            if self.num % 3 == 1 or self.num % 3 == 0:
                screen.blit(self.imgs[9], self.rect)
                return 0
            else:
                screen.blit(self.imgs[0], self.rect)
                return 0

        if press_keys[K_DOWN]:

            self.rect.top += self.speed
            # ����������޷����ƶ�
            if self.rect.bottom >= 510:
                self.rect.bottom = 510
            # �ж��Ƿ���ײ��70��һ���������ϰ��﷽��߳�
            for n in range(len(block_group)-1):
                if self.rect.left > block_group[n].rect.left - 70 and self.rect.right < block_group[n].rect.right + 70:
                    if self.rect.top < block_group[n].rect.top < self.rect.bottom:
                        self.rect.top -= self.speed
                        break
            # ��������if...else����ʹ�����˲��������ƶ�ʱ�Ķ���
            if self.num % 3 == 1 or self.num % 3 == 0:
                screen.blit(self.imgs[3], self.rect)
                return 0
            else:
                screen.blit(self.imgs[0], self.rect)
                return 0

        # ���ڲ�����ֹʱ�Ķ���
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