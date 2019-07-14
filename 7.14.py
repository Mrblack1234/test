# -*- coding: gb2312 -*-
import numpy as np
'''
a=np.inf         #����
print(type(a))

b=np.nan         #û����ֵ
print(type(b))

#print(np.nan==np.nan)    #false

#�ж�������nan�ĸ���===================================
t=np.array([1.,2.,0])
t[2]=np.nan
print(t)
print(np.count_nonzero(t))                #ͳ���������治Ϊ0�ĸ���

print(np.count_nonzero(t!=t))             #ͳ����������Ϊnan�ĸ���
print(np.isnan(t))                        #[False False  True]
print(np.count_nonzero(np.isnan(t)))      #ͳ����������Ϊnan�ĸ���

'''
#nan���κ�ֵ���㶼��nan
#1+2+3+nan==nan
'''

t2=np.arange(12).reshape((3,4)).astype(int)

print(t2)

d=np.mean(t2)          #�鿴�����е�ƽ��ֵ
e=np.average(t2)       #�鿴�����е�ƽ��ֵ
print(d)
print(e)

f=np.median(t2)        #�鿴�����е���λ��
print(f)

g=np.cumsum(t2)         #�Ծ����е����������ۼ�
print(g)

g=np.max(t2,axis=1)         #�Ծ����е����������ۼ�
print(g)

g=np.min(t2,axis=1)         #�Ծ����е����������ۼ�
print(g)

g=np.ptp(t2)           #��ֵ�����ֵ����Сֵ֮��
print(g)

g=np.std(t2)           #��׼��
print(g)


t2=np.arange(12).reshape((3,4)).astype(float)

t2[1,2:]=np.nan
print(t2)

#����1
def fill_mean(t1):
    for i in range(t1.shape[1]):
        temp_col = t1[:, i]
        nan_num = np.count_nonzero(temp_col != temp_col)
        if nan_num != 0:
            temp_non_nan = temp_col[temp_col == temp_col]    #��ǰһ�в�Ϊnan��array
            temp_col[np.isnan(temp_col)] = temp_non_nan.mean()  #temp_col[np.isnan(temp_col)]��ʾ�����е�nan

    return  t1


print(fill_mean(t2))

'''
#pandans����ѧϰ========================================================================================
import pandas as pd
import string
'''
==========pandas���õ���������==================
Seriesһά������ǩ(index)����
Dataframe��ά��Series����
'''

'''
#ͨ���б����ʽ����Series
t=pd.Series([1,2,3,4,5,6])
print(t)
print(type(t))
t2=pd.Series([1,2,3,4,5,],index=list('abcde'))    #ָ������
print(t2)
#ͨ���ֵ����ʽ����Series
temp_dict={"name":"xiaohong","age":30,"tel":10086}
t3=pd.Series(temp_dict)
print(t3)

temp_dict1={string.ascii_uppercase[i]:i for i in range(10)}
print(temp_dict1)
t4=pd.Series(temp_dict1)
print(t4)

t5=pd.Series(t4,index=list(string.ascii_uppercase[5:15]))
print(t5)

#�޸����ֵ�����astype/dtype
t6=t2.astype('float')
print(t6)

#==========pandas֮Series��Ƭ������==================
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
#��������====================
print(t[t>2])

#Serirs�������;����ֵ====================
temp_dict={"name":"xiaohong","age":30,"tel":10086}
t3=pd.Series(temp_dict)
print(t3.index)
print(t3.values)
print('*'*100)
print(t3.keys)
#����index�ı���
for i in t3.index:
    print(i)
#����index������
print(type(t3.index))
#��ȡindex�ĳ���
print(len(t3.index))
#ת����list
print(list(t3.index)[:1])

'''
'''
#pandas֮��ȡ�ⲿ������====================
df=pd.read_excel('dog_name.xlsx')
#print(df)
#dataframe��ʹ��==========================
d1=pd.DataFrame(np.arange(12).reshape((3,4)))
print(d1)
'''
'''
   0  1   2   3     #������
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11

#������
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
print(d2.ndim)            #��ʾ���ݵ�ά��
print(d2.head(2))         #��ʾ���ݵ�ǰ����
print(d2.tail(2))         #��ʾ���ݵ�ĩβ����
print(d2.info())          #��ʾ���ݵľ������Ϣ
print(d2.describe())      #��ʾ���ֵ�ͳ����Ϣ
'''
'''
#����dataframe��������
df=df.sort_values(by="times")           #�Դ�����������(��������)
print(df)
#��ʾ����ʮ������
print(df.tail(10))
#��ʾǰ��ʮ������
df=df.sort_values(by="times",ascending=False)      #�Դ����������򣨽������У�
print(df.head(10))
'''

#pandas֮ȡ��ȡ��==========================
#[]ȡ���ֱ�ʾ���н��в������ַ�����ʾ���н��в���
'''
print(df[:5])   #ȡ���ݵ�ǰ5��
print(df["times"])   #ȡ����times��
print(type(df["times"]))
#pandas֮loc==========================
'''
#df.locͨ����ǩ����������

t3=pd.DataFrame(np.arange(12).reshape((3,4)),index=list('abc'),columns=list("qwer"))
'''
print(t3)
print(t3.loc["a","q"])
print(t3.loc["a"])
print(t3.loc[:,"q"])
print(t3.loc[["a","b"]])
print(t3.loc[:,["w","e"]])
print(t3.loc[["a","b"],["w","e"]])  #ð����loc�����Ǳպϵ�
'''
#df.ilocͨ��λ�û�ȡ������
'''
print(df.iloc[0])
print(df.iloc[:,0])
print(df.iloc[:,[0,1]])

df.iloc[:,0]=np.nan

print(df)
'''
'''
#pandas֮��������=============================================
t1=df[df["times"]>1000]
print(t1)

#��ʾȡtimes�������600С��1000������\
#&��ʾ��=======|��ʾ��
t2=df[(df["times"]<1000)&(df["times"]>600)]
print(t2)

t3=df[(df["dog_name"].str.len()>4)&(df["times"]>600)]
print(t3)
'''
#==========================.str.split("/").tolist() ��ʾͨ���ָ�����series��Ȼ�������б�================

#pandas֮ȱʧ���ݵĴ���=============================================
#�ж��Ƿ���nan
t3=pd.DataFrame(np.arange(12).reshape((3,4)),index=list('abc'),columns=list("qwer"))
t3.iloc[[0,2],[1,3]]=np.nan
'''
print(t3)
print(pd.isnull(t3))   #�ж��Ƿ���nan������true
print(pd.notnull(t3))   #�ж��Ƿ���nan������false

t3=t3[pd.isnull(t3['r'])]  # r��һ��Ϊnan����Ӧ����
print(t3)

#ɾ��nan���л�����
t4=t3.dropna(axis=1)  #��ʾɾ������nan����
print(t4)

t5=t3.dropna(axis=1,how="all")
print(t5)

t6=t3.dropna(axis=1,how="any")
print(t6)

t7=t3.dropna(axis=1,how="any",inplace=True)  #��֮ǰ��dataframe�����޸�
print(t7)
'''
print(t3)

print(t3.fillna(0))    #��nan�����ݽ������

print(t3.fillna(t3.mean()))    #��nan�����ݽ������

print(t3["r"].fillna(t3["r"].mean()))    #��r�е�����nan�����ݽ������
t3["r"]=t3["r"].fillna(t3["r"].mean())
print(t3)

#����Ϊ0������
#==t[t==0]=np.nan  �����е�Ϊ0�����ݱ��nan






