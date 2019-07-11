import pandas as pd
from datetime import date,timedelta,datetime,time
from dateutil.parser import	parse
"""
"""
#基本的函数介绍===============================================================
"""
#enumerate函数========================================
#Python内建了⼀个enumerate函数，可以返回(i,value)元组序列：
some_list=['foo','bar','baz']
mapping	={}
for i, v in enumerate(some_list):
    mapping[v] = i
print(mapping)

#sorted函数========================================
#sorted函数可以从任意序列的元素返回⼀个新的排好序的列表：
a_sorted=sorted([7,	1,	2,	6,	0,	3,	2])
print(a_sorted)

b_sorted=sorted('horse	race')
print(b_sorted)

#zip函数========================================
#zip可以将多个列表、元组或其它序列成对组合成⼀个元组列表：

seq1=['foo','bar','baz']
seq2=['one','two','three']
zipped=zip(seq1,seq2)
zippedd=list(zipped)
print(zippedd)

first_names,last_names=zip(*zippedd)

print(first_names)
print(last_names)

#reversed函数========================================
#reversed可以从后向前迭代⼀个序列：
a_list=list(reversed(range(10)))
print(a_list)


"""
#字典介绍============================================================================
"""
d1={'a'	:'somevalue','b':[1,2,3,4]}

print(d1)
#直接插入字典
d1[7]='an interger'
print(d1)
#{'a': 'somevalue', 'b': [1, 2, 3, 4], 7: 'an interger'}
#直接显示b对应的内容
print(d1['b'])

#删除相应的内容
#del关键字直接删除内容
del d1[7]
print(d1)
#pop关键字直接删除内容并且返回删除的值
ret = d1.pop('b')
print(ret)
print(d1)

#keys和values是字典的键和值的迭代器⽅法
d1={'a'	:'somevalue','b':[1,2,3,4]}
print(d1.keys())
print(d1.values())

#update⽅法是原地改变字典，因此任何传递给update的键的旧的值都会被舍弃。
d1.update({'b':'hdd','v':'sGGg'})
print(d1)

#⽤序列创建字典
#方法1
mapping_1={}
for key,value in zip(range(5),reversed(range(5))):
    mapping_1[key]=value
print(mapping_1)
#方法2
mapping_2=dict(zip(range(5),reversed(range(5))))
print(mapping_2)



#默认值
some_dict_1={1:2,3:4,5:6}
#方法1编写函数
def key_if_in_some_dict(key,some_dict,default_value):
    if key in some_dict:
        value = some_dict[key]
    else:
        value = default_value
    print(value)
key_if_in_some_dict(90,some_dict_1,6)

#方法2 dict的⽅法get和pop可以取默认值进⾏返回
value=some_dict_1.pop(90,4)
print(value)

#你可以通过⾸字⺟，将⼀个列表中的单词分类
words = ['apple','bat',	'bar',	'atom',]
by_letter = {}
for word in words:
    letter = word[0]
    if letter not in by_letter:
        by_letter[letter] = [word]
    else:
        by_letter[letter].append(word)

print(by_letter)

#setdefault⽅法就正是⼲这个的。前⾯的for循环可以改写为
for	word in	words:
	letter = word[0]
	by_letter.setdefault(letter,[]).append(word)
print(by_letter)

#集合
#集合是无序的不可重复的元素的集合。
#通过set函数
print(set([2,2,2,1,3,3]))
#尖括号set语句
print({2,2,2,1,3,3})

#合并是取两个集合中不重复的元素
a	=	{1,	2,	3,	4,	5}
b	=	{3,	4,	5,	6,	7,	8}
c=a.union(b)
print(c)

#交集的元素包含在两个集合中。
d=a.intersection(b)
print(d)

d=a.copy()
d|=b
print(d)
"""

#列表、集合和字典推导式=====================================================
"""
列表推导式是Python最受喜爱的特性之⼀。它允许⽤户⽅便的从
⼀个集合过滤元素，形成列表，在传递参数的过程中还可以修改
元素。形式如下：
[expr	for	val	in	collection	if	condition]
它等同于下⾯的for循环;
result	=	[]
for	val	in	collection:
	if	condition:
		 result.append(expr)

#列表
strings	=['a','as','bat','car','dove']

strings_1=[x.upper() for x in strings if len(x)>=2]

print(strings_1)

#字典

#???????????????????????????????????????????????????????????????
some_list=['foo','bar','baz']
mapping	={}
for i, v in enumerate(some_list):
    mapping[v] = i
print(mapping)

string={val:index for index,val in enumerate(some_list)}
print(string)

#集合的推导式
#选取列表中的字符串长度来生成set
some_list=['foo','bar','baz']
some_list_1={len(x) for x in some_list}
print(some_list_1)
#或者or
some_list_2=set(map(len,some_list))
print(some_list_2)
"""


#函数============================================================
"""
def	func():
	a	=	[]
	for	i	in	range(5):
		a.append(i)
print(a)
"""
a = []
def	func_1():
	for	i	in	range(5):
		a.append(i)
print(a)

def	f():
	a	=	5
	b	=	6
	c	=	7
	return	a,	b,	c
a,	b,	c	=	f()
print(a)
print(b)
print(c)

#返回元组
return_value	=	f()
print(return_value)

#返回字典
def	f_1():
	a = 5
	b =	6
	c =	7
	return	{'a': a, 'b' : b, 'c' :	c}
return_value_1 = f_1()
print(return_value_1)

#函数也是对象
#正则表达式re模块
import	re
def	clean_strings(strings):
				result	=	[]
				for	value	in	strings:
					value	=	value.strip()                   #去除开头和结尾的空格
					value	=	re.sub('[!#?]',	'',	value)      #用正则表达式进行替换
					value	=	value.title()                   #对每一个单词开头大写
					result.append(value)
				return	result

state=	['			Alabama	',	'Georgia!',	'Georgia',	'georgia',	'FlOrIda','southcarolina##']

print(clean_strings(state))

#???????????????????????????????????????????????????????????????????????????????????????????????
states=	['			Alabama	',	'Georgia!',	'Georgia',	'georgia',	'FlOrIda','southcarolina##']
def	remove_punctuation(value):
    return re.sub('[!#?]', '', value)
clean_ops	=	[str.strip,	remove_punctuation,	str.title]
def	clean_strings(strings,	ops):
				result	=	[]
				for	value	in	strings:
								for	function	in	ops:
												value	=	function(value)
								result.append(value)
				return	result
print(clean_strings(states,	clean_ops))
