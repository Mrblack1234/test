# -*- coding: gb2312 -*-
import numpy as np
'''
a=np.inf         #无限
print(type(a))

b=np.nan         #没有数值
print(type(b))

#print(np.nan==np.nan)    #false

#判断数组中nan的个数===================================
t=np.array([1.,2.,0])
t[2]=np.nan
print(t)
print(np.count_nonzero(t))                #统计数组里面不为0的个数

print(np.count_nonzero(t!=t))             #统计数组里面为nan的个数
print(np.isnan(t))                        #[False False  True]
print(np.count_nonzero(np.isnan(t)))      #统计数组里面为nan的个数

'''
#nan和任何值计算都是nan
#1+2+3+nan==nan
'''

t2=np.arange(12).reshape((3,4)).astype(int)

print(t2)

d=np.mean(t2)          #查看矩阵中的平均值
e=np.average(t2)       #查看矩阵中的平均值
print(d)
print(e)

f=np.median(t2)        #查看矩阵中的中位数
print(f)

g=np.cumsum(t2)         #对矩阵中的数进行逐步累加
print(g)

g=np.max(t2,axis=1)         #对矩阵中的数进行逐步累加
print(g)

g=np.min(t2,axis=1)         #对矩阵中的数进行逐步累加
print(g)

g=np.ptp(t2)           #极值，最大值和最小值之差
print(g)

g=np.std(t2)           #标准差
print(g)


t2=np.arange(12).reshape((3,4)).astype(float)

t2[1,2:]=np.nan
print(t2)

#方法1
def fill_mean(t1):
    for i in range(t1.shape[1]):
        temp_col = t1[:, i]
        nan_num = np.count_nonzero(temp_col != temp_col)
        if nan_num != 0:
            temp_non_nan = temp_col[temp_col == temp_col]    #当前一列不为nan的array
            temp_col[np.isnan(temp_col)] = temp_non_nan.mean()  #temp_col[np.isnan(temp_col)]表示数组中的nan

    return  t1


print(fill_mean(t2))

'''
#pandans内容学习========================================================================================
import pandas as pd
import string
'''
==========pandas常用的数据类型==================
Series一维，带标签(index)数组
Dataframe二维，Series容器
'''

'''
#通过列表的形式创建Series
t=pd.Series([1,2,3,4,5,6])
print(t)
print(type(t))
t2=pd.Series([1,2,3,4,5,],index=list('abcde'))    #指定索引
print(t2)
#通过字典的形式创建Series
temp_dict={"name":"xiaohong","age":30,"tel":10086}
t3=pd.Series(temp_dict)
print(t3)

temp_dict1={string.ascii_uppercase[i]:i for i in range(10)}
print(temp_dict1)
t4=pd.Series(temp_dict1)
print(t4)

t5=pd.Series(t4,index=list(string.ascii_uppercase[5:15]))
print(t5)

#修改数字的类型astype/dtype
t6=t2.astype('float')
print(t6)

#==========pandas之Series切片和索引==================
temp_dict={"name":"xiaohong","age":30,"tel":10086}
t3=pd.Series(temp_dict)
print(t3)

print(t3['age'])
print(t3[1])

print(t3[[0,2]])

print(t3[['age',"tel"]])


t=pd.Series([1,2,3,4,5,6])
print(t)

print(t[1:3])
print(t[1:3:2])
#布尔索引====================
print(t[t>2])

#Serirs的索引和具体的值====================
temp_dict={"name":"xiaohong","age":30,"tel":10086}
t3=pd.Series(temp_dict)
print(t3.index)
print(t3.values)
print('*'*100)
print(t3.keys)
#关于index的遍历
for i in t3.index:
    print(i)
#关于index的类型
print(type(t3.index))
#获取index的长度
print(len(t3.index))
#转化成list
print(list(t3.index)[:1])

'''
'''
#pandas之读取外部的数据====================
df=pd.read_excel('dog_name.xlsx')
#print(df)
#dataframe的使用==========================
d1=pd.DataFrame(np.arange(12).reshape((3,4)))
print(d1)
'''
'''
   0  1   2   3     #行索引
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11

#列索引
'''
'''
d1=pd.DataFrame(np.arange(12).reshape((3,4)),index=list('abc'),columns=list('abcd'))
print(d1)

d2={"name":["qwe","dfui"],"age":[20,15],"tel":[10086,10010]}
d2=pd.DataFrame(d2)
'''
'''
print(d2.values)
print(d2.index)
print(d2.columns)
print(d2.shape)
print(d2.dtypes)
print(d2.ndim)            #表示数据的维度
print(d2.head(2))         #显示数据的前几行
print(d2.tail(2))         #显示数据的末尾几行
print(d2.info())          #显示数据的具体的信息
print(d2.describe())      #显示数字的统计信息
'''
'''
#利用dataframe进行排序
df=df.sort_values(by="times")           #对次数进行排序(升序排列)
print(df)
#显示后面十个数据
print(df.tail(10))
#显示前面十个数据
df=df.sort_values(by="times",ascending=False)      #对次数进行排序（降序排列）
print(df.head(10))
'''

#pandas之取行取列==========================
#[]取数字表示对行进行操作，字符串表示对列进行操作
'''
print(df[:5])   #取数据的前5行
print(df["times"])   #取具体times列
print(type(df["times"]))
#pandas之loc==========================
'''
#df.loc通过标签索引行数据

t3=pd.DataFrame(np.arange(12).reshape((3,4)),index=list('abc'),columns=list("qwer"))
'''
print(t3)
print(t3.loc["a","q"])
print(t3.loc["a"])
print(t3.loc[:,"q"])
print(t3.loc[["a","b"]])
print(t3.loc[:,["w","e"]])
print(t3.loc[["a","b"],["w","e"]])  #冒号在loc里面是闭合的
'''
#df.iloc通过位置获取行数据
'''
print(df.iloc[0])
print(df.iloc[:,0])
print(df.iloc[:,[0,1]])

df.iloc[:,0]=np.nan

print(df)
'''
'''
#pandas之布尔索引=============================================
t1=df[df["times"]>1000]
print(t1)

#表示取times里面大于600小于1000的数据\
#&表示且=======|表示或
t2=df[(df["times"]<1000)&(df["times"]>600)]
print(t2)

t3=df[(df["dog_name"].str.len()>4)&(df["times"]>600)]
print(t3)
'''
#==========================.str.split("/").tolist() 表示通过分割生成series，然后生成列表================

#pandas之缺失数据的处理=============================================
#判断是否有nan
t3=pd.DataFrame(np.arange(12).reshape((3,4)),index=list('abc'),columns=list("qwer"))
t3.iloc[[0,2],[1,3]]=np.nan
'''
print(t3)
print(pd.isnull(t3))   #判断是否是nan，返回true
print(pd.notnull(t3))   #判断是否是nan，返回false

t3=t3[pd.isnull(t3['r'])]  # r这一列为nan所对应的行
print(t3)

#删除nan的行或者列
t4=t3.dropna(axis=1)  #表示删除带有nan的列
print(t4)

t5=t3.dropna(axis=1,how="all")
print(t5)

t6=t3.dropna(axis=1,how="any")
print(t6)

t7=t3.dropna(axis=1,how="any",inplace=True)  #对之前的dataframe进行修改
print(t7)
'''
print(t3)

print(t3.fillna(0))    #对nan的数据进行填充

print(t3.fillna(t3.mean()))    #对nan的数据进行填充

print(t3["r"].fillna(t3["r"].mean()))    #对r列的数据nan的数据进行填充
t3["r"]=t3["r"].fillna(t3["r"].mean())
print(t3)

#处理为0的数据
#==t[t==0]=np.nan  对所有的为0的数据变成nan






