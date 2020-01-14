#!/usr/bin/python2
"""
A function to find the difference betweeen the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sum_square_difference():
    sequence = range(1, 101)
    sum_of_squares = sum(i**2 for i in sequence)
    square_of_sum = sum(sequence)**2
    print(square_of_sum - sum_of_squares)

sum_square_difference()
