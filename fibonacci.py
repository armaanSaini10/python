# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 15:45:13 2022

@author: armaa
"""

def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
fib(14)
            