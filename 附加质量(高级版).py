# -*- coding: gb2312 -*-
'''
path=input('�����ļ�����')       #��������·��
outfile=input('����ļ�����')     #�������·��
'''
path='abaqus1.rpt' #����·��
outfile='abaqus1.txt'

f_in=open(path,'r',encoding='gbk')        #�ļ�������
f_out=open(outfile,'w',encoding='gbk')    #�ļ�������
KT=0
TYPE=0
ELEM_NUM=40000       #��Ԫ��Ŀ
#print(f_in.read())
for line in f_in:
    if KT==19:
        if line.split()==[]:
            break
        else:
            line_1 = line.split()
            TYPE += 1
            ELEM_NUM += 1
            f_out.write("*USER ELEMENT,LINEAR,NODES=1,TYPE=U%04d\n" % TYPE)
            f_out.write("   1,2,3\n")
            f_out.write("*MATRIX,TYPE=MASS\n")
            f_out.write("   %s\n" % abs(float(line_1[1])))
            f_out.write("   0,   %s\n" % abs(float(line_1[2])))
            f_out.write("   0,   0,   %s\n" % abs(float(line_1[3])))
            f_out.write("*ELEMENT,ELSET=ADD,TYPE=U%04d\n" % TYPE)
            f_out.write("   %s,   %s\n" % (ELEM_NUM, line_1[0]))
    else:
        KT += 1
f_out.write("*Uel property,Elset=ADD,Alpha=0\n")






















