# -*- coding: gb2312 -*-
#格式化输出
age=18
print(age)
#=======%s 表示字符串
#=======%d 表示有符号的十进制整数
#=======%f 表示浮点数

name='tim'

weight=75.5

stu_id=1
stu_i=1000
for i in range(10):
    print("今年我%d岁" % (i+1))


print("我叫%s" % name)

print("我的体重是%f"%weight)

print("我的体重是%.2f"%weight)    #2表示小数的位数是两位

print("今年我学号%d" % stu_id)

print("今年我学号%03d" % stu_id)   #学号是3位，其他位用0来补齐

print("今年我学号%03d" % stu_i)   #学号是3位，其他位用0来补齐

print("我的体重是%.2f，今年我学号%d"%(weight,stu_id))

print("我的体重是%.2f，今年我学号%d"%(weight,stu_id+1))

print("我的体重是%s，今年我学号%s"%(weight,stu_id+1))

#f'{表达式}' 字符串更加高效
print(f'我的体重是{name},今年我学号{stu_id}')


#转义字符==================================================================
#\n换行
#\t制表符，一个tab键（4个空格）的距离
print("hello,\nworld")

print("hello,\tworld")

#结束符
print("===========================================================")
print("hello,world=========================")
print("hello,world",end="\n")  #默认是这个换行符
print("hello,world",end="\t")
print("hello,world",end="---------")
print("hello,world")

'''
#=============================================================================
#格式化输入
aaaa=input("提示信息：")
print(aaaa)
'''



#format的用法

print('{0},{1}'.format('zhangk', 32))

print('{},{},{}'.format('zhangk','boy',32))

print('{name},{sex},{age}'.format(age=32,sex='male',name='zhangk'))


















