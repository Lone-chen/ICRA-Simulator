
def get_lines(x1, y1, x2, y2):
    """
    输入起点终点坐标,返回一个包含线段上各点的list
    :return: [(a1,b1),....] (ai,bi)为包含于线段的坐标点
    """
    if x1 <= x2 :
       return get_lines_(x1, y1, x2, y2)
    else:
       return get_lines_(x2, y2, x1, y1)



def get_lines_(x1, y1, x2, y2):
    """
    (x1,y1)(x2,y2) 满足x1<=x2
    :return: [(a1,b1),....] (ai,bi)为包含于线段的坐标点
    """
    line = []
    if y1 >= y2:
        bottom = y1
        for i in range(x1, x2+1):
            flag = False
            for j in range(bottom,y2-1,-1):
                if judge_fuc(x1,y1,x2,y2,i,j):
                    line.append((i, j))
                    flag = True
                else:
                    if flag == False:
                        bottom = j
                    else:
                        break
    else:
        top = y1
        for i in range(x1, x2+1):
            flag = False
            for j in range(top, y2+1):
                if judge_fuc(x1,y1,x2,y2,i,j):
                    line.append((i, j))
                    flag = True
                else:
                    if flag == False:
                        top = j
                    else:
                        break
    return line

def judge_fuc(x1, y1, x2, y2, xp, yp):
    if x1 == x2:
        if xp == x1 and yp >= y1 and yp <= y2:
            return True
        else:
            return False
    else:
        k = (y2 - y1) / (x2 - x1)
        fy = (xp - x1) * k + y1
        dx = 0.99
        dy = (xp + dx -x1) * k + y1
        if yp == int(fy) or (yp > int(fy) and yp <= int(dy)):
            # print(xp,yp,fy,dy)
            return True
        else:
            return False

# print(judge_fuc(30,40,58,45,35,41))
# print(get_lines(30,40,58,45))


if __name__ == '__main__':
    import numpy as np
    import cv2
    x = np.zeros((1000,1000))
    list = get_lines(300,400,120,123)
    print(list)
    for p,q in list:
        x[p][q] = 255
    cv2.namedWindow('image')
    cv2.imshow('image',x)
    cv2.waitKey(0)

