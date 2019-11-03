import random

class MAP(object):
    def __init__(self):
        # 地图单位像素大小为1mm×1mm
        self.length = 8100  # 地图横向长度
        self.width = 5100   # 地图纵向长度
        self.map = []       # 存放地图信息,初始化全部为0
        self.areas = []     # 判定区域为加成区（红/蓝）/禁区

        self.barrier_start = ([0,1000],[1500,2425],[1500,4100],[3600,1000],[3600,3850],[6350,0],[5800,2425],[7100,3850])  # 障碍物左上角坐标(B1-B4,B6-B9)
        self.barrier_end = ([1000,1250],[2300,2675],[1750,5100],[4400,1250],[4400,4100],[6600,1000],[6600,2675],[8100,4100])  # 障碍物右上角坐标(B1-B4,B6-B9)
        self.area_start = ([230,1500],[1630,2925],[3730,270],[7330,3120],[5930,1695],[3730,4350])  # 加成区/禁区左上角坐标
        self.area_end = ([770,1980],[2170,3405],[4270,750],[7870,3600],[6470,2175],[4270,4830])  # 加成区/禁区右下角坐标

    def map_initialization(self):  # 将地图的每一个像素格对应的数组元素初始化为0
        l=[]
        x,y=1,1

        while x <= 5100:  # 5100行
            while y <= 8100:  # 8100列
                l.append(0)
                y = y + 1
            self.map.append(l)
            l = []
            x = x + 1
            y = 1

    def map_barriers(self):  # 将障碍物区域对应的数组元素赋值为1
        for i in range(9):
            for m in range(self.barrier_start[i][1] , self.barrier_end[i][1]+1):
                for n in range(self.barrier_start[i][0] , self.barrier_end[i][0]+1):
                    self.map[m][n] = 1

    def map_areas(self):  # 将不同区域对应的数组元素赋值为2-7（6个不同功能区域）
        for i in range(6):
            for m in range(self.area_start[i][1] , self.area_end[i][1]+1):
                for n in range(self.area_start[i][0] , self.area_end[i][0]+1):
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

    def areas_rand(self):  # 加成区/禁区随机更新
        self.areas[0] = random.randint(2,7)  # 为F1和F4随机更新
        if self.areas[0] % 2 == 0:
            self.areas[3] = self.areas[0] + 1
        else:
            self.areas[3] = self.areas[0] - 1

        self.areas[1] = self.areas[0]  # 为F2和F5随机更新
        while self.areas[1] == self.areas[0] or self.areas[1] == self.areas[3]:
            self.areas[1] = random.randint(2,7)
        if self.areas[1] % 2 == 0:
            self.areas[4] = self.areas[1] + 1
        else:
            self.areas[4] = self.areas[1] - 1

        for i in range(2,8):  # 更新F3和F6
            if i != self.areas[0] and i != self.areas[1] and i != self.areas[3] and i != self.areas[4]:
                self.areas[2]=i
        if self.areas[2] % 2 == 0:
            self.areas[5] = self.areas[2] + 1
        else:
            self.areas[5] = self.areas[2] - 1

