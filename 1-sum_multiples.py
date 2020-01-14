#!/usr/bin/python3
def sum_multiples():
    """ A function to sum all the numbers multiples of 3 and 5 bellow 1000 """
    """ Solution using generator expression """

    print(sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0))


""" Calling the function """
sum_multiples()
    
