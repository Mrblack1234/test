# -*- coding: gb2312 -*-
#��ʽ�����
age=18
print(age)
#=======%s ��ʾ�ַ���
#=======%d ��ʾ�з��ŵ�ʮ��������
#=======%f ��ʾ������

name='tim'

weight=75.5

stu_id=1
stu_i=1000
for i in range(10):
    print("������%d��" % (i+1))


print("�ҽ�%s" % name)

print("�ҵ�������%f"%weight)

print("�ҵ�������%.2f"%weight)    #2��ʾС����λ������λ

print("������ѧ��%d" % stu_id)

print("������ѧ��%03d" % stu_id)   #ѧ����3λ������λ��0������

print("������ѧ��%03d" % stu_i)   #ѧ����3λ������λ��0������

print("�ҵ�������%.2f��������ѧ��%d"%(weight,stu_id))

print("�ҵ�������%.2f��������ѧ��%d"%(weight,stu_id+1))

print("�ҵ�������%s��������ѧ��%s"%(weight,stu_id+1))

#f'{���ʽ}' �ַ������Ӹ�Ч
print(f'�ҵ�������{name},������ѧ��{stu_id}')


#ת���ַ�==================================================================
#\n����
#\t�Ʊ����һ��tab����4���ո񣩵ľ���
print("hello,\nworld")

print("hello,\tworld")

#������
print("===========================================================")
print("hello,world=========================")
print("hello,world",end="\n")  #Ĭ����������з�
print("hello,world",end="\t")
print("hello,world",end="---------")
print("hello,world")

'''
#=============================================================================
#��ʽ������
aaaa=input("��ʾ��Ϣ��")
print(aaaa)
'''



#format���÷�

print('{0},{1}'.format('zhangk', 32))

print('{},{},{}'.format('zhangk','boy',32))

print('{name},{sex},{age}'.format(age=32,sex='male',name='zhangk'))


















