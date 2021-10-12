# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 00:01:14 2021

@author: Administrator
"""

import random

#随机获取一个[1,100]之间的整数 x
x = random.randint(1,101)
print(x)


#定义一个函数，获取从 1 RMB到得到 x RMB的最少moves的次数
#分析：对于x来说，除以2会比减1更快的到达1
def Least_moves(x):
    count = 0
    if x == 1:
        return 0
    while x > 1: 
        if x % 2 == 0: 
            x = x / 2 #若为偶数，则直接除以2
            count = count + 1   
        else:
            x = x - 1 #若为奇数则减1后再进入while循环除以2
            count = count + 1
    return count

least_moves = Least_moves(x)
print(least_moves)
    
