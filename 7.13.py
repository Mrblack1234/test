# -*- coding: gb2312 -*-
'''
Numpy��ʹ�÷���
'''

import numpy as np
import random
'''
#numpy������====================================================
array=np.array([[1,2,3],
               [1,2,3]])
print(array)

print("number of dim:",array.ndim)   #�����ά��
print("shape:",array.shape)          #�������״
print("size:",array.size)            #����Ԫ�صĸ���


#����numpy��������================================================
#a=np.array([1,21,3,4],dtype=np.int64)
a=np.array([1,21,3,4],dtype=np.float64)
print(a)
print(a.dtype)

aa=np.array([[1,21,3,4],
             [2,3,4,55]],dtype=np.int64)
print(aa)
print(aa.dtype)

#����ȫ��Ϊ0�ľ���
a0=np.zeros((3,4),dtype=np.int64)
print(a0)
#����ȫ��Ϊ1�ľ���
a1=np.ones((3,4),dtype=np.int64)
print(a1)
#���ɵ�λ����
print(np.eye(10))


#����ȫ��Ϊempty�ľ���
a1=np.empty((3,4))
print(a1)
#��������ľ���
a1=np.arange(12,20,2)
print(a1)

a1=np.arange(12).reshape((3,4))
print(a1)

a1=np.linspace(1,10,20)          #����һ��1-10�����У�����Ϊ20
print(a1)

'''
#numpy�Ļ�������====================================================
'''
a=np.array([[10,20],
            [30,40]])
b=np.arange(4).reshape((2,2))

c=a-b
d=a+b
e=b**2
f=np.sin(a)       #������ȡsin
g=10*np.cos(a)    #������ȡcos
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(b<3)

m=a*b          #�����е�ÿ�����
print(m)
f=np.dot(a,b)  #�������
g=a.dot(b)     #�������,��np.dot(a,b)�ȼ�
print(f)
print(g)


a=np.random.random((2,4))   #����0-1�м��������ֵľ���
print(a)

b=np.sum(a)
c=np.max(a)
d=np.min(a)

print(b,c,d)

b=np.sum(a,axis=1)    #axis=1��ʾ������ȡ��
c=np.max(a,axis=0)    #axis=0��ʾ������ȡ���ֵ
d=np.min(a)
print(b,c,d)

A=np.arange(2,14).reshape((3,4))
print(A)

b=np.argmin(A)        #�鿴��������Сֵ��Ӧ������
c=np.argmax(A)        #�鿴���������ֵ��Ӧ������
print(b)
print(c)


b=np.argmin(A,axis=0)        #�鿴��������Сֵ��Ӧ������
c=np.argmax(A,axis=0)        #�鿴���������ֵ��Ӧ������
print(b)
print(c)



d=np.mean(A)          #�鿴�����е�ƽ��ֵ
e=np.average(A)       #�鿴�����е�ƽ��ֵ
print(d)
print(e)

f=np.median(A)        #�鿴�����е���λ��
print(f)

g=np.cumsum(A)         #�Ծ����е����������ۼ�
print(g)

h=np.diff(A)          #�Ծ����е��������۲�
print(h)

i=np.sort(A)          #����ֵ������������
print(i)

print(A.T)              #����ֵ����װ��

print(np.clip(A,5,9))   #�ھ����У�С��5����������5������9����������9
'''

#numpy��index====================================================
'''
a=np.arange(3,15)
print(a)
print(a[3])

a=np.arange(3,15).reshape((3,4))


print(a)

print(a[2])         #��ʾ����
print(a[:2])        #��ʾȡǰ����
print(a[2][2])      #ȡ�����е����е�����
print(a[2,2])       #ȡ�����е����е�����
print(a[:,2])       #ȡ�����е�����
print(a[2,:])       #ȡ�����е�����
print(a[2,1:3])     #ȡ������,1-2������

for row in  a:       #��ÿһ�д�ӡ����
    print(row)

for column in a.T:   #��ÿһ�д�ӡ����
    print(column)

for item in a.flat:  #��ÿһ���������ֵ��ӡ����
    print(item)

#numpy��array�ϲ�====================================================
a=np.array([1,2,3,4])
b=np.array([3,4,5,6])

print(np.vstack((a,b)))   #�������µĺϲ�
print(np.hstack((a,b)))   #�������ҵĺϲ�

print(a[:,np.newaxis])

a=np.array([1,2,3,4])[:,np.newaxis]
b=np.array([3,4,5,6])[:,np.newaxis]

print(np.hstack((a,b)))   #�������ҵĺϲ�

c=np.concatenate((a,b,a,b),axis=1)   #�Զ��ά�Ƚ��к���ϲ�
c=np.concatenate((a,b,a,b),axis=0)   #�Զ��ά�Ƚ�������ϲ�

print(c)


#numpy��array�ָ�====================================================
a=np.arange(12).reshape((3,4))
print(a)

#print(np.split(a,2,axis=1))   #�������������ľ��ȷָ�

#print(np.split(a,3,axis=0))    #��������к���ľ��ȷָ�

print(np.array_split(a,3,axis=1))   #�������������Ĳ����ȷָ�

print(np.vsplit(a,3))         #��������к���ľ��ȷָ�

print(np.hsplit(a,2))         #�������������ľ��ȷָ�


#numpy��array����====================================================

a=np.array([1,2,3,4])
print(a)

b=a
c=a
d=a

print(b,c,d)

c[0]=33

print(b,c,d)    #ǣһ����ȫ��


b=a.copy()     #deep cpy

a[1]=100
print(b,a)


array=np.array([[1,2,3],[1,2,3]])
print(array)
'''
#=============================================================================
'''
a=np.arange(24)      #1ά����
print(a)
print(a.shape)
b=a.reshape(2,3,4)   #3ά���飨.reshape����ı�����ԭ�������ݣ�������һ���µ����飩
print(b)
c=b.reshape(24,)
print(c)
d=b.reshape(24,1)     #����2ά���飬24�У�1��
print(d)
e=b.reshape(1,24)     #����2ά���飬1�У�24��
print(e)


a=np.arange(24).reshape((4,6))  
print(a)

b=a.reshape((a.shape[0]*a.shape[1],))  #���1ά����

#a.shape��ʾa����״
#a.shape[0]��ʾa������
#a.shape[1]��ʾa������

print(b)

c=a.flatten()                       #���1ά����
print(c)


a=np.arange(24).reshape((4,6))
print(a)

print(a+2)     #����������ÿһ��ֵ������2

print(a*2)     #����������ÿһ��ֵ������2

print(a/2)     #����������ÿһ��ֵ������2

#print(a/0)

#����״һ��ʱ����Ӧ������ֱ�����

b=np.array([0,1,2,3,4,5])
print(b.shape)
print(a-b)

c=np.arange(4).reshape((4,1))
print(c)

print(a-c)

#������������
t5=np.array([1,2,0,0,1,0,2],dtype=bool)
print(t5)

print(t5.dtype)

t6=t5.astype('int32')               #������������
print(t6)
print(t6.dtype)

#np�е�С��
t7=np.array([random.random() for i in range(10)])    #���������
print(t7)

#�����ɵ�����λС��
t8=np.round(t7,2)
print(t8)

a=np.arange(3,15).reshape((3,4))

print(a)
print("="*100)
print(a[2,1:])             #��ʾ����

print("="*100)
print(a[:,[0,2]])           #��ʾ����
print("="*100)
print(a[[0,2],:])         #��ʾȡ���У�����ȡ1��3���У�

a=np.arange(3,15).reshape((3,4))

a[a>10]=100
print(a)

#print(np.where(a<6,100,300))

#print(np.clip(A,5,9))   #�ھ����У�С��5����������5������9����������9

#�Բ�ͬ�е����ݽ��н���
a[[1,2],:]=a[[2,1],:]    #�н���
print(a)
a[:,[1,2]]=a[:,[2,1]]    #�н���
print(a)

print(np.eye(10).astype("int"))  #���ɶԽǵľ���
'''

##numpy���������====================================================
#print(np.random.randint(10,20,(4,5)))    #����10-20��4��5�����2ά����

np.random.seed(10)
print(np.random.randint(10,20,(4,5)))    #ֻ����һ������Ľ��(ÿ�ε���������һ����)
































