# -*- coding: utf-8 -*-
"""
Created on Sat May 23 11:22:51 2020

@author: User
"""
from random import randrange
from time import time,sleep
def LinearSearch(ans):
    sTime=time()
    for i in range(100000000):
        if  ans==i:
            print("線性搜尋法:花了"+str(time()-sTime)+"秒")
            break
def BinarySearch(ans):
    sTime=time()
    low=0
    upper=100000000
        while <=upper:
            mid=(low+upper)//2
            if mid<r:
                low=mid+1
            
            elif mid>r:
                upper=mid-1
            
            else:
                print("二元搜尋法:花了"+str(time()-sTime)+"秒")
                return
        
LinearSearch(10)
LinearSearch(10000)
LinearSearch(1000000)
BinarySearch(10)
BinarySearch(10000)
BinarySearch(1000000)