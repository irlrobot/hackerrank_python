#!/bin/python3
"""
https://www.hackerrank.com/challenges/py-if-else/problem
If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
"""


num = int(input())

if (num % 2) == 1:
    print("Weird")
else:
    if num in list(range(2, 5)):
        print("Not Weird")
    elif num in list(range(6, 20)):
        print("Weird")
    elif num > 20:
        print("Not Weird")
