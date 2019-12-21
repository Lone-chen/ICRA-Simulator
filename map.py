import random

class MAP(object):
    def __init__(self):
        # 地图单位像素大小为1mm×1mm
        self.length = 8100  # 地图横向长度
        self.width = 5100   # 地图纵向长度
        self.map = []       # 存放地图信息,初始化全部为0
        self.areas = [2, 3, 4, 5, 6, 7]     # 判定区域为加成区（红/蓝）/禁区

        self.barrier_start = ([0, 100], [150, 242], [150, 410], [350, 100], [350, 385], [635, 0], [580, 242], [710, 385])  # 障碍物左上角坐标(B1-B4,B6-B9)
        self.barrier_end = ([100, 125], [230, 267], [175, 510], [450, 125], [450, 410], [660, 100], [660, 267], [810, 410])  # 障碍物右上角坐标(B1-B4,B6-B9)
        self.area_start = ([23, 150], [163, 292], [373, 27], [733, 312], [593, 169], [373, 435])  # 加成区/禁区左上角坐标
        self.area_end = ([77, 198], [217, 340], [427, 75], [787, 360], [647, 217], [427, 483])  # 加成区/禁区右下角坐标
        self.map_initialization()
        self.areas_rand()
        self.map_barriers()
        self.map_areas()



    def map_initialization(self):  # 将地图的每一个像素格对应的数组元素初始化为0
        l=[]
        x,y=1,1

        while x <= 510:  # 510行
            while y <= 810:  # 810列
                l.append(0)
                y = y + 1
            self.map.append(l)
            l = []
            x = x + 1
            y = 1

    def areas_rand(self):  # 加成区/禁区随机更新
        self.areas[0] = random.randint(2, 7)  # 为F1和F4随机更新
        if self.areas[0] % 2 == 0:
            self.areas[3] = self.areas[0] + 1
        else:
            self.areas[3] = self.areas[0] - 1

        self.areas[1] = self.areas[0]  # 为F2和F5随机更新
        while self.areas[1] == self.areas[0] or self.areas[1] == self.areas[3]:
            self.areas[1] = random.randint(2, 7)
        if self.areas[1] % 2 == 0:
            self.areas[4] = self.areas[1] + 1
        else:
            self.areas[4] = self.areas[1] - 1

        for i in range(2, 8):  # 更新F3和F6
            if i != self.areas[0] and i != self.areas[1] and i != self.areas[3] and i != self.areas[4]:
                self.areas[2] = i
        if self.areas[2] % 2 == 0:
            self.areas[5] = self.areas[2] + 1
        else:
            self.areas[5] = self.areas[2] - 1

    def map_barriers(self):  # 将障碍物区域对应的数组元素赋值为1
        for i in range(8):
            for m in range(self.barrier_start[i][1] , self.barrier_end[i][1]):
                for n in range(self.barrier_start[i][0] , self.barrier_end[i][0]):
                    self.map[m][n] = 1
        for i in range(0, 15):
            for j in range(404 - i, 405 + i):
                self.map[i + 240][j] = 1
        for i in range(0, 15):
            for j in range(390 + i, 419 - i):
                self.map[i + 255][j] = 1
        for i in range(0, 6):
            for j in range(404 - i, 405 + i):
                self.map[i + 249][j] = 8
        for i in range(0, 6):
            for j in range(399 + i, 410 - i):
                self.map[i + 255][j] = 8


    def map_areas(self):  # 将不同区域对应的数组元素赋值为2-7（6个不同功能区域）
        for i in range(6):
            for m in range(self.area_start[i][1] , self.area_end[i][1]):
                for n in range(self.area_start[i][0] , self.area_end[i][0]):
                    if self.areas[i] == 2:
                        self.map[m][n] = 2  # 红方回血区

                    elif self.areas[i] == 3:
                        self.map[m][n] = 3  # 蓝方回血区

                    elif self.areas[i] == 4:
                        self.map[m][n] = 4  # 红方弹药补给区

                    elif self.areas[i] == 5:
                        self.map[m][n] = 5  # 蓝方弹药补给区

                    elif self.areas[i] == 6:
                        self.map[m][n] = 6  # 禁止移动区

                    else:
                        self.map[m][n] = 7  # 禁止射击区


mp = MAP()
print(mp.areas)
