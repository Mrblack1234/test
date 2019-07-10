import pandas as pd
from datetime import date,timedelta,datetime,time
from dateutil.parser import	parse
"""
#datetime.datetime类型数据
start=datetime(2019,7,25,8,10,20)
print(start)
print(start.day)                                   #显示天
print(start.minute)                                #显示分钟
print(start.hour)                                  #显示小时
print(type(start))
print('============================================================')

#将datetime.datetime数据类型转化成str类型
start_1=start.strftime('%Y-%m-%d %H:%M:%S')        #记得大小写
print(start_1)
print(type(start_1))
print('============================================================')

#把str类型转化成datetime.datetime类型
start_2=datetime.strptime('2010-10-31','%Y-%m-%d')
print(start_2)
print(type(start_2))

#显示现在的时刻
print(datetime.now())
print('============================================================')

#时刻替换
start_3=datetime(2019,7,25,8,10,20)
print(start_3)
start_4=start_3.replace(year=2010)
print(start_4)
print('============================================================')



#在datetime.datetime类型中时刻进行相减，必须使用timedelta库
start_3=datetime(2014,7,25,8,10,50)
start_5=datetime(2019,7,25,8,10,20)
delta=start_5-start_3
print(delta)
print(type(delta))    #delta属于datetime.timedelta类型
print('============================================================')

#在一个时间上面加一个时间段
start_6=timedelta(days=1856,minutes=20)
print(start_6+start_3)
print(type(start_6+start_3))      #start_6+start_3属于datetime.datetime类型
print('============================================================')


#将datetime.datetime数据类型转化成str类型
start_7=datetime(2019,7,25)
print(str(start_7))
start_8=start_7.strftime('%Y-%m-%d')        #记得大小写
print(start_8)
print(type(start_8))
print('============================================================')


#把str类型转化成datetime.datetime类型
start_9=parse('2010-10-31')
print(start_9)
print(type(start_9))
start_10=datetime.strptime('2010-10-31','%Y-%m-%d')
print(start_10)
print(type(start_10))
print('============================================================')


#元组
tup=(4,5,6)
print(tup)

tup_1=(4,5,6),(6,7)
print(tup_1)

#tuple函数将任意的序列转化为元组
tup_2=tuple([4,0,2])
print(tup_2)

tup_3=tuple('bwifawg')     #元组创建后，各个位置的对象无法修改
print(tup_3)

#元组可以直接相加
tup_4=(4,5,6)+(4,5,6)+(4,5,6)
print(tup_4)

tup_5=(4,5,6)*4
print(tup_5)

#元组中数据的提取

tup_6=(4,5,6)
a,b,c=tup_6
print(a)

#交换两个数
a,b=1,2
print(a)
print(b)
a,b=b,a
print(a)
print(b)

#查找a里面有几个2
a=1,2,2,3,4,5,6,7,4,6,4,3
a_count=a.count(2)
print(a_count)
print('============================================================')


#列表list，长度可以变，内容可以修改
a_list=[1,2,3,5,None]    #None中的N必须大写
print(a_list)

b_list=1,2,3,5,None
print(b_list)

c_list=list(b_list)
print(c_list)

#列表相加
print([1,2,2]+['e',456,4,5])
x=[1,2,2]
x.extend(['e',456,4,5])          #注意！！！！！！！！！！！！！！！用extend速度更加的快
print(x)
print('============================================================')



#list函数常⽤来在数据处理中实体化迭代器或⽣成器
gen=range(10)
print(gen)
print(list(gen))


#
b_list=	['foo',	'peekaboo',	'baz']
b_list.append('dwarf')                         #在末尾上添加
print(b_list)
#insert可以在特定的位置插⼊元素
b_list.insert(1, 'red')                #insert可以在特定的位置插⼊元素
print(b_list)
#insert的逆运算是pop，它移除并返回指定位置的元素
b_list.pop(2)
print(b_list)
#可以⽤remove去除某个值，remove会先寻找第⼀个值并除去
b_list.remove('foo')
print(b_list)

#排序============================================================
#你可以⽤sort函数将⼀个列表原地排序
a_sort=	[7,	2,	5,	1,	3]
a_sort.sort()
print(a_sort)

#⼆级排序key
b_sort= ['saw', 'small', 'He', 'foxes', 'six']
b_sort.sort(key=len)
print(b_sort)

#⼆分搜索和维护已排序的列表
import	bisect
c_bisect=[1,2,2,2,3,4,7]
d_bisect=bisect.bisect(c_bisect,2)   #按顺序插入值并找出这个值的位置
print(d_bisect)
print(c_bisect)
#bisect模块不会检查列表是否已排好序，进⾏检查的话会耗费⼤量计算。因此，对未排序的列表使⽤bisect不会产⽣错误，但结果不⼀定正确。
"""

#切⽚
#切⽚的基本形式是在⽅括号中使⽤start:stop：
#切⽚的起始元素是包括的，不包含结束元素
seq = [7, 2, 3, 7, 5, 6, 0, 1]
print(seq[1:2])
seq[1:2]=[100]
print(seq)

print(seq[:2])

print(seq[1:])

print(seq[::2])      #在第⼆个冒号后⾯使⽤step，可以隔⼀个取⼀个元素

print(seq[::-1])     #⼀个聪明的⽅法是使⽤-1，它可以将列表或元组颠倒过来


































































