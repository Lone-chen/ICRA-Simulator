import operator
import datetime
import numpy as np
from numpy import *
from os import listdir
from skimage import io

print('程序处理的图片大小,建议不要超过200*200\n')
N = int(input('需要处理的图片的大小(100至200)，N='))
#N = 120            # 图片大小：N*N
color = 100/255  # 灰度阈值

#KNN算法主体
def KNN(test_data,train_data,train_label,k):
    #已知分类的数据集(训练集)的行数
    dataSetSize = train_data.shape[0]
    #求所有距离：tile函数将输入点拓展成与训练集相同维数的矩阵，并计算测试样本与每一个训练样本的距离
    all_distances = np.sqrt(np.sum(np.square(tile(test_data,(dataSetSize,1))-train_data),axis=1))
    #按all_distances中元素进行升序排序后得到其对应索引的列表
    sort_distance_index = all_distances.argsort()
    #选择距离最小的k个点
    all_predictive_value = {}
    for i in range(k):
        #返回最小距离的训练集的索引(预测值)
        predictive_value = train_label[sort_distance_index[i]]
        print('第',i+1,'次预测值',predictive_value)
        all_predictive_value[predictive_value] = all_predictive_value.get(predictive_value,0)+1
    #求众数：按classCount字典的第2个元素（即类别出现的次数）从大到小排序
    sorted_class_count = sorted(all_predictive_value.items(), key = operator.itemgetter(1), reverse = True)
    return sorted_class_count[0][0]

#训练集：得到训练集数据矩阵、下标签索引
def get_all_train_data():
    train_label = []
    train_file_list = listdir('train_data')  #获取目录内容
    m = len(train_file_list)                       #m维向量的训练集
    #get_train_data函数：得到所有训练集图像的向量矩阵
    train_data = get_all_data(train_file_list,1)
    for i in range(m):
        file_name = train_file_list[i]        #fileNameStr:所有训练集文件名
        train_label.append(get_number_cut(file_name))    #得到训练集下标
    return train_label,train_data

#得到所有训练集/测试集的向量矩阵（k=1训练集传入；k=0测试集传入）
def get_all_data(file_list,k):
    train_data = np.zeros([len(file_list), N**2])
    #enumerate函数用于遍历序列中的元素以及它们的下标（i是下标，item是元素信息）
    for i, item in enumerate(file_list):
        if k == 1:
            #训练集：读取图片并转为灰度值(黑字体为0，白底为255)
            img = io.imread('./train_data/'+ item, as_grey = True)
        else:
            #测试集：读取图片并转为灰度值(黑字体为0，白底为255)
            img = io.imread('./test_list/' + item, as_grey = True)
        #降噪处理
        img[img>color] = 1
        #将图片进行切割，保留有值的部分
        img = get_cut_picture(img)
        #将图片进行拉伸，得到需求大小：N*N
        img = get_stretch_picture(img).reshape(N**2)
        #将处理后的图片信息存入矩阵
        train_data[i, 0:N**2] = img
        #若将图片的真实值存入矩阵(需要存入图片索引，上面语句改train_data = np.zeros([len(file_list), N**2+1])
        #train_data[i, N**2] = float(item[0])
    return train_data

#切割图象
def get_cut_picture(img):
    #初始化新大小
    size = []
    #图片的行数
    length = len(img)
    #图片的列数
    width = len(img[0,:])
    #计算新大小
    size.append(get_edge(img, length, 0, [-1, -1]))
    size.append(get_edge(img, width, 1, [-1, -1]))
    size = np.array(size).reshape(4)
    #print('图像尺寸（高低左右）：',size)
    return img[size[0]:size[1]+1, size[2]:size[3]+1]

#获取切割边缘(高低左右的索引)
def get_edge(img, length, flag, size):
    for i in range(length):
        #判断是行是列
        if flag == 0:
            #正序判断该行是否有手写数字
            line1 = img[img[i,:]<color]
            #倒序判断该行是否有手写数字
            line2 = img[img[length-1-i,:]<color]
        else:
            line1 = img[img[:,i]<color]
            line2 = img[img[:,length-1-i]<color]
        #若有手写数字，即到达边界，记录下行
        if len(line1)>=1 and size[0]==-1:
            size[0] = i
        if len(line2)>=1 and size[1]==-1:
            size[1] = length-1-i
        #若上下边界都得到，则跳出
        if size[0]!=-1 and size[1]!=-1:
            break
    return size

#拉伸图像
def get_stretch_picture(img):
    newImg = np.ones(N**2).reshape(N, N)
    newImg1 = np.ones(N ** 2).reshape(N, N)
    #对每一行/列进行拉伸/压缩
    #每一行拉伸/压缩的步长
    step1 = len(img[0])/N
    #每一列拉伸/压缩的步长
    step2 = len(img)/N
    #对每一行进行操作
    for i in range(len(img)):
        for j in range(N):
            newImg[i, j] = img[i, int(np.floor(j*step1))]
    #对每一列进行操作
    for i in range(N):
        for j in range(N):
            newImg1[j, i] = newImg[int(np.floor(j*step2)), i]
    return newImg1

#从文件名中分解出第一个数字（真实值）
def get_number_cut(file_name):
    classNumStr = str(file_name.split('_')[0])
    return classNumStr

#用字符矩阵打印图片
def get_show(test_data):
	for i in range(N**2):
		if(test_data[0,i] == 0):
			print ("1",end='')
		else:
			print ("0",end='')
		if (i+1)%N == 0 :
			print()

def main():
    t1 = datetime.datetime.now()  # 计时开始
    Nearest_Neighbor_number = int(input('选取最邻近的K个值(建议小于7)，K='))
    #训练集：get_train_data()函数得到训练集数据矩阵、下标签索引
    train_label, train_data = get_all_train_data()

    #测试集：根据路径，获取测试集地址
    test_file_list = listdir('test_list')
    file_name = test_file_list[0]
    #测试集：运用切片函数，得到测试集下标索引(真实值)
    test_index = get_number_cut(file_name)
    #测试集：得到训练集图像的向量矩阵
    test_data = get_all_data(test_file_list,0)
    #测试集：get_show()函数：用字符矩阵打印图片
    get_show(test_data)

    #调用knn算法进行测试
    Result = KNN(test_data, train_data, train_label, Nearest_Neighbor_number)
    print ("最终预测值为:",Result)
    print ("     真实值:",test_index)
    t2 = datetime.datetime.now()
    print('耗 时 = ', t2 - t1)

if __name__ == "__main__":
    main()