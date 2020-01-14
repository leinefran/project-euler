#!/usr/bin/python2
"""
A function to find the smallest positive number that is evenly divisible by all the numbers from 1 to 20.
"""
def smallest_multiple(step):
    check_list = [11, 13, 14, 16, 17, 18, 19, 20]
    for num in xrange(step, 999999999, step):
        if all(num % n == 0 for n in check_list):
            return num
    return None

if __name__ == '__main__':
    solution = smallest_multiple(20)
    if solution is None:
        print "No answer found"
    else:
        print "found an answer:", solution
