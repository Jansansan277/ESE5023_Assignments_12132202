# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 21:22:36 2021

@author: Administrator
"""

import numpy as np


#2.1: 定义一个用numpy来创建维度为c×d,取数范围为[a,b)随机整数的矩阵的函数
#方法参考自: https://www.cnblogs.com/pipiyan/p/10445948.html
def create_matrix(a,b,c,d): 
    M = np.random.randint(a,b,size=(c,d)) #创建一个c×d二维整数数组也即是矩阵,取数范围为[a,b)随机整数
    print(M,type(M))
    return M

#2.1: 使用create_matrix()函数创建M1(5×10),M2(10×5),取数范围均为[0,51)随机整数
M1 = create_matrix(0,51,5,10) 
M2 = create_matrix(0,51,10,5)


#2.2: 定义两个矩阵做乘法的函数
#方法参考自: https://www.runoob.com/python/python-exercise-example44.html
def matrix_multiplication(A=[[]],B=[[]]): #A，B默认值为空的二维array
    M =[]
    if (len(A)==len(B[0])) and (len(A[0])==len(B)): #len(A)表示矩阵A的行数，len(A[0])表示矩阵A的列数
        for i in range(len(A)): #迭代A的行
            R = [] #存储乘法运算后第i行的结果
            for j in range(len(A)): #迭代B的列
                Mij = 0 #用来存储 M矩阵第i行第j列结果
                for k in range(len(A[0])): # 将A的第i行元素和B的第j行元素对应相乘后累加求和
                    Mij = Mij + A[i][k] * B[k][j]
                R.append(Mij) #存储累加求和后的结果到第i行列表中
            M.append(R) #将第i行存入M矩阵中
    else:
        print('Sorry, the matrics you input cannot be multiplicated!')
    return M

#2.2: 使用matrix_mulyiplication()函数做M1和M2的乘法
M = matrix_multiplication(M1,M2)
print('\nThe multiplication result is:\n',np.matrix(M)) #将M转换为matrix格式输出



#若将M1，M2从array转换为matrix类型可以直接做乘法运算如下,可以用来检验上述for循环得到的乘法运算是否正确
'''
M1 = np.matrix(M1)
M2 = np.matrix(M2)
M_validation = M1*M2
print(M_validation)
print(M==M_validation)
'''   
        





