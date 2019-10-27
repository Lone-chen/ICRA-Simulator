import random
class map(object):
    def __init__(self, length, width, barriers, areas):
        self.length = 810
        self.width = 510
        self.map = []
        self.areas = []

        self.barrier_start = ([],[],[],[],[],[],[],[])
        self.barrier_end = ([],[],[],[],[],[],[],[])
        self.area_start = ([],[],[],[],[],[])
        self.area_end = ([],[],[],[],[],[])

    def MAP(self):
        l=[]
        x,y=1,1

        while x <= 510:
            while y <= 810:
                l.append(0)
                y = y + 1
            self.map.append(l)
            l = []
            x = x + 1
            y = 1

    def BARRIERS(self):
        for i in range(9):
            for m in range(self.barrier_start[i][1] , self.barrier_end[i][1]+1):
                for n in range(self.barrier_start[i][0] , self.barrier_end[i][0]+1):
                    self.map[m][n] = 1

    def AREAS(self):
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

    def RABD(self):
        self.areas[0] = random.randint(2,7)
        if self.areas[0] % 2 == 0:
            self.areas[3] = self.areas[0] + 1
        else:
            self.areas[3] = self.areas[0] - 1

        self.areas[1] = self.areas[0]
        while self.areas[1] == self.areas[0] and self.areas[1] == self.areas[3]:
            self.areas[1] = random.randint(2,7)
        if self.areas[1] % 2 == 0:
            self.areas[4] = self.areas[1] + 1
        else:
            self.areas[4] = self.areas[1] - 1

        for i in range(2,8):
            if i != self.areas[0] and i != self.areas[1] and i != self.areas[3] and i != self.areas[4]:
                self.areas[2]=i
        if self.areas[2] % 2 == 0:
            self.areas[5] = self.areas[2] + 1
        else:
            self.areas[5] = self.areas[2] - 1
