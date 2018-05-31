#!/bin/python3
import os
import sys
#
# Complete the solve function below.
#
def solve(a0, a1, a2, b0, b1, b2):
    a_score = 0
    b_score = 0

    if a0 > b0:
        a_score += 1
    if b0 > a0:
        b_score += 1
    if a1 > b1:
        a_score += 1
    if b1 > a1:
        b_score += 1
    if a2 > b2:
        a_score += 1
    if b2 > a2:
        b_score += 1
    
    return(a_score, b_score)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    a0A1A2 = input().split()
    a0 = int(a0A1A2[0])
    a1 = int(a0A1A2[1])
    a2 = int(a0A1A2[2])
    b0B1B2 = input().split()
    b0 = int(b0B1B2[0])
    b1 = int(b0B1B2[1])
    b2 = int(b0B1B2[2])

    result = solve(a0, a1, a2, b0, b1, b2)
    f.write(' '.join(map(str, result)))
    f.write('\n')
    f.close()