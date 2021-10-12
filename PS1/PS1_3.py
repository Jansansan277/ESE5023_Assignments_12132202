# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 21:32:10 2021

@author: Administrator
"""
'''
print(list(range(30, 0, -2)))
range(start,stop,step),注意stop处的数字是不包含的
'''

#定义一个生成二维array形式的帕斯卡三角形的函数,加上下标返回第N-1行
#此方法参考了：https://blog.csdn.net/swansonge/article/details/107522978
def pascal_triangle(N):
    PT = [] #定义一个空列表存放帕斯卡三角形的所有行
    for layer in range(N):
        if layer == 0:
            PT.append([1]) 
        elif layer == 1:
            PT.append([1,1]) #帕斯卡三角形的头两行需要自己定义好
        else:
            tempList = get_layer(layer,PT[layer-1])
            PT.append(tempList)
    return PT[N-1] 

#定义一个生成杨辉三角形的第三行及之后的行的函数，基于重要的数学特征：除去首尾之外的元素等于两肩的元素和
#此方法参考了：http://blog.sina.com.cn/s/blog_b33f67290102w5f7.html
def get_layer(layer,L): #layer代表行数，L代表上一行的所有元素构成的列表
    tempList = [] #每次创建一个空列表以存储当前所求行
    for i in range(layer+1):
        if i == 0 or i == layer: #首尾元素均为1
            tempList.append(1)
        else: #中间元素等于两肩（上一行）的元素和
            tempList.append(L[i-1] + L[i])
    return tempList

#打印输出N阶杨辉三角的的第N行
N = 200 #指定杨辉三角的阶数
L = pascal_triangle(N) #获取N阶杨辉三角的第N行
print(L) #打印输出结果

            