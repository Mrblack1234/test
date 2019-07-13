# -*- coding: gb2312 -*-
'''
Numpy的使用方法
'''

import numpy as np
import random
'''
#numpy的属性====================================================
array=np.array([[1,2,3],
               [1,2,3]])
print(array)

print("number of dim:",array.ndim)   #数组的维数
print("shape:",array.shape)          #数组的形状
print("size:",array.size)            #数组元素的个数


#利用numpy生成数组================================================
#a=np.array([1,21,3,4],dtype=np.int64)
a=np.array([1,21,3,4],dtype=np.float64)
print(a)
print(a.dtype)

aa=np.array([[1,21,3,4],
             [2,3,4,55]],dtype=np.int64)
print(aa)
print(aa.dtype)

#生成全部为0的矩阵
a0=np.zeros((3,4),dtype=np.int64)
print(a0)
#生成全部为1的矩阵
a1=np.ones((3,4),dtype=np.int64)
print(a1)
#生成单位矩阵
print(np.eye(10))


#生成全部为empty的矩阵
a1=np.empty((3,4))
print(a1)
#生成有序的矩阵
a1=np.arange(12,20,2)
print(a1)

a1=np.arange(12).reshape((3,4))
print(a1)

a1=np.linspace(1,10,20)          #生成一个1-10的数列，个数为20
print(a1)

'''
#numpy的基础运算====================================================
'''
a=np.array([[10,20],
            [30,40]])
b=np.arange(4).reshape((2,2))

c=a-b
d=a+b
e=b**2
f=np.sin(a)       #对数组取sin
g=10*np.cos(a)    #对数组取cos
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(b<3)

m=a*b          #矩阵中的每个相乘
print(m)
f=np.dot(a,b)  #矩阵相乘
g=a.dot(b)     #矩阵相乘,与np.dot(a,b)等价
print(f)
print(g)


a=np.random.random((2,4))   #生成0-1中间的随机数字的矩阵
print(a)

b=np.sum(a)
c=np.max(a)
d=np.min(a)

print(b,c,d)

b=np.sum(a,axis=1)    #axis=1表示在列中取和
c=np.max(a,axis=0)    #axis=0表示在行中取最大值
d=np.min(a)
print(b,c,d)

A=np.arange(2,14).reshape((3,4))
print(A)

b=np.argmin(A)        #查看矩阵中最小值对应的索引
c=np.argmax(A)        #查看矩阵中最大值对应的索引
print(b)
print(c)


b=np.argmin(A,axis=0)        #查看矩阵中最小值对应的索引
c=np.argmax(A,axis=0)        #查看矩阵中最大值对应的索引
print(b)
print(c)



d=np.mean(A)          #查看矩阵中的平均值
e=np.average(A)       #查看矩阵中的平均值
print(d)
print(e)

f=np.median(A)        #查看矩阵中的中位数
print(f)

g=np.cumsum(A)         #对矩阵中的数进行逐步累加
print(g)

h=np.diff(A)          #对矩阵中的数进行累差
print(h)

i=np.sort(A)          #对数值进行逐行排序
print(i)

print(A.T)              #对数值进行装置

print(np.clip(A,5,9))   #在矩阵当中，小于5的数都等于5，大于9的数都等于9
'''

#numpy的index====================================================
'''
a=np.arange(3,15)
print(a)
print(a[3])

a=np.arange(3,15).reshape((3,4))


print(a)

print(a[2])         #表示行数
print(a[:2])        #表示取前两行
print(a[2][2])      #取第三行第三列的数字
print(a[2,2])       #取第三行第三列的数字
print(a[:,2])       #取第三列的数字
print(a[2,:])       #取第三行的数字
print(a[2,1:3])     #取第三行,1-2的数字

for row in  a:       #把每一行打印出来
    print(row)

for column in a.T:   #把每一列打印出来
    print(column)

for item in a.flat:  #把每一个具体的数值打印出来
    print(item)

#numpy的array合并====================================================
a=np.array([1,2,3,4])
b=np.array([3,4,5,6])

print(np.vstack((a,b)))   #进行上下的合并
print(np.hstack((a,b)))   #进行左右的合并

print(a[:,np.newaxis])

a=np.array([1,2,3,4])[:,np.newaxis]
b=np.array([3,4,5,6])[:,np.newaxis]

print(np.hstack((a,b)))   #进行左右的合并

c=np.concatenate((a,b,a,b),axis=1)   #对多个维度进行横向合并
c=np.concatenate((a,b,a,b),axis=0)   #对多个维度进行纵向合并

print(c)


#numpy的array分割====================================================
a=np.arange(12).reshape((3,4))
print(a)

#print(np.split(a,2,axis=1))   #对数组进行纵向的均等分割

#print(np.split(a,3,axis=0))    #对数组进行横向的均等分割

print(np.array_split(a,3,axis=1))   #对数组进行纵向的不均等分割

print(np.vsplit(a,3))         #对数组进行横向的均等分割

print(np.hsplit(a,2))         #对数组进行纵向的均等分割


#numpy的array复制====================================================

a=np.array([1,2,3,4])
print(a)

b=a
c=a
d=a

print(b,c,d)

c[0]=33

print(b,c,d)    #牵一发动全身


b=a.copy()     #deep cpy

a[1]=100
print(b,a)


array=np.array([[1,2,3],[1,2,3]])
print(array)
'''
#=============================================================================
'''
a=np.arange(24)      #1维数组
print(a)
print(a.shape)
b=a.reshape(2,3,4)   #3维数组（.reshape不会改变数组原来的内容，会生成一个新的数组）
print(b)
c=b.reshape(24,)
print(c)
d=b.reshape(24,1)     #生成2维数组，24行，1列
print(d)
e=b.reshape(1,24)     #生成2维数组，1行，24列
print(e)


a=np.arange(24).reshape((4,6))  
print(a)

b=a.reshape((a.shape[0]*a.shape[1],))  #变成1维数组

#a.shape表示a的形状
#a.shape[0]表示a的行数
#a.shape[1]表示a的列数

print(b)

c=a.flatten()                       #变成1维数组
print(c)


a=np.arange(24).reshape((4,6))
print(a)

print(a+2)     #给数组里面每一个值都加上2

print(a*2)     #给数组里面每一个值都乘上2

print(a/2)     #给数组里面每一个值都除以2

#print(a/0)

#当形状一样时，对应的数字直接相加

b=np.array([0,1,2,3,4,5])
print(b.shape)
print(a-b)

c=np.arange(4).reshape((4,1))
print(c)

print(a-c)

#调整数据类型
t5=np.array([1,2,0,0,1,0,2],dtype=bool)
print(t5)

print(t5.dtype)

t6=t5.astype('int32')               #调整数据类型
print(t6)
print(t6.dtype)

#np中的小数
t7=np.array([random.random() for i in range(10)])    #生成随机数
print(t7)

#对生成的数两位小数
t8=np.round(t7,2)
print(t8)

a=np.arange(3,15).reshape((3,4))

print(a)
print("="*100)
print(a[2,1:])             #表示行数

print("="*100)
print(a[:,[0,2]])           #表示列数
print("="*100)
print(a[[0,2],:])         #表示取多行（这里取1，3两行）

a=np.arange(3,15).reshape((3,4))

a[a>10]=100
print(a)

#print(np.where(a<6,100,300))

#print(np.clip(A,5,9))   #在矩阵当中，小于5的数都等于5，大于9的数都等于9

#对不同列的数据进行交换
a[[1,2],:]=a[[2,1],:]    #行交换
print(a)
a[:,[1,2]]=a[:,[2,1]]    #列交换
print(a)

print(np.eye(10).astype("int"))  #生成对角的矩阵
'''

##numpy生成随机数====================================================
#print(np.random.randint(10,20,(4,5)))    #生成10-20的4乘5的随机2维数列

np.random.seed(10)
print(np.random.randint(10,20,(4,5)))    #只生成一个随机的结果(每次的随机结果是一样的)
































