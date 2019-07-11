import pandas as pd
from datetime import date,timedelta,datetime,time
from dateutil.parser import	parse
"""
#匿名（lambda）函数
#关键字没有别的含义，仅仅是说“我们正在声明的是⼀个匿名函数”。
def	short_function(x):
	return	x	*	2

equiv_anon	=	lambda	x:	x	*	2

#===========================================
def	apply_to_list(some_list,f):
				return	[f(x)	for	x	in	some_list]
ints	=	[4,	0,	1,	5,	6]
ints_1=apply_to_list(ints,	lambda	x:	x*2)
print(ints_1)

strings = ['foo', 'card', 'bar', 'aaaa', 'abab']

"""
#sorted()不会改变原来的list，而是会返回一个新的已经排序好的list
#list.sort()方法仅仅被list所定义，sorted()可用于任何一个可迭代对象
"""

strings_1=list(strings)
print(strings_1)
strings_2=set(strings_1)
print(strings_2)
strings_3=strings.sort(key=lambda x:len(set(list(x))))    #key表示排序的依据
print(strings)

strings_4 = ['foo', 'card', 'bar', 'aaaa', 'abab']
strings_5=sorted(strings_4,key=lambda x:len(set(list(x))))
print(strings_4)
print(strings_5)

#生成器================================================================================
some_dict	=	{'a':	1,	'b':	2,	'c':	3}
for	values	in	some_dict:
    print(values)

dict_iterator	=	iter(some_dict)
print(dict_iterator)
print(list(dict_iterator))      #调用后只能用一次

dict_iterator	=	iter(some_dict)
print(dict_iterator)
print(tuple(dict_iterator))

dict_iterator	=	iter(some_dict)
print(dict_iterator)
print(min(dict_iterator))

dict_iterator	=	iter(some_dict)
print(dict_iterator)
print(max(dict_iterator))

a=[1,2,3,4,5,6,7,8,9,10]
for i in a:
    print(a.index(i))

for i in range(0,len(a)):
    print(a[i])
print(len(a))


a=[1,2,3,4,5,6,7,8,9,10]
iter_1=iter(a)
print(next(iter_1))

print(next(iter_1))

#生成器表达式
#把列表推导式两端的⽅括号改成圆括号
gen	=	(x	**	2	for	x	in	range(100))
print(gen)
print(list(gen))

gen	=	((x,x ** 2)	for	x	in	range(10))
print(dict(gen))


#itertools模块
#groupby可以接受任何序列和⼀个函数。它根据函数的返回值对序列中的连续元素进⾏分组。
import	itertools
first_letter	=	lambda	x:	x[0]
names = ['Alan', 'Adam', 'Wes', 'Will', 'Albert','Steven']

for	letter,	names	in	itertools.groupby(names,	first_letter):
			print(letter,	list(names))


#读写文件============================================================================
path='7.11.txt'
f = open(path,'r',encoding='utf8').read()
print(f)

path_1='7.111.txt'
#f = open(path,encoding='gbk').read()
f = open(path_1,'w',encoding='gbk')    #文件句柄
f.write("比较AB v吧你HFio,\n")
f.write("比较AB v吧你HFio\n")

path_1='7.111.txt'
f = open(path_1,'a',encoding='gbk')    #append表示追加
f.write("sgngdn共患难是给是德国,\n")
f.write("首页你 事业部水嫩让用户")
f.close()

"""
'''
path_1='7.11.txt'
f = open(path_1,'r',encoding='utf8')
'''
#f.readline()表示读取一行
#读取前5行
#for i in range(5):
#    print(f.readline())

#strip表示把空格和换行都去掉
#方法1
#for index,line in enumerate(f.readlines()):
#    if index !=9:
#        print(line.strip())

#方法2
'''
for index,line in enumerate(f.readlines()):
#    print(line)
    if index ==9:
        print('===============================')
        continue
    print(line.strip())
'''
'''
#方法3  加一个计数器
count=0
for line in f:
#    print(line)
    count+=1
    if count == 10:
        print('===============================')
        continue
    print(line.strip())
    print(count)
'''
'''
count=0
for line in f:
    if count == 10:
        print('===============================')
        count += 1
        continue
    print(line.strip())
    count += 1
    print(count)
'''
'''
print(f.tell())
print(f.read(5))    #读取前五个字符
print(f.tell())
print(f.readline())    #读取第一行字符
print(f.readline())    #读取第一行字符
print(f.readline())    #读取第一行字符
print(f.tell())        #显示指针的位置
f.seek(0)              #将指针的位置放在最开始
print(f.readline())
print(f.encoding)      #打印编码
print(f.name)          #打印文件名
'''
'''
path_1='7.11.txt'
#f = open(path_1,'r+',encoding='gbk')   #读写（读取一个文件，然后写）
f = open(path_1,'w+',encoding='gbk')    #写读（先创建一个文件，然后读）
print(f.readline())    #读取第一行字符
print(f.readline())    #读取第一行字符
print(f.readline())    #读取第一行字符
print(f.tell())
f.write("======================================")
print(f.readline())    #读取第一行字符
print(f.readline())    #读取第一行字符

print(f.read())


path_1='7.11.txt'
f = open(path_1,'w+',encoding='gbk')    #写读（先创建一个文件，然后读）
f.write("===============hello====================\n")
f.write("===============hello====================\n")
f.write("===============hello====================\n")
f.write("===============hello====================\n")
print(f.tell())
f.seek(10)
print(f.readline())
f.write("===============22====================")
'''





