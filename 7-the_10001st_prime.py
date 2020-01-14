#!/usr/bin/python2
"""
A function to find the 10001st prime number.
"""

import math

'''Checks if a number is a prime'''
def is_prime(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

'''Finds the value for the given nth term'''
def term(n):
    x = 0
    count = 0
    while count != n:
        x += 1
        if is_prime(x) == True:
            count += 1
    print x


term(10001)
