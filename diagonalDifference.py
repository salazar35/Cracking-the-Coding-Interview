#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the diagonalDifference function below.
#
def diagonalDifference(a):
    #
    # Write your code here.
    #
    n = len(a)
    s1 = 0
    s2 = 0
    for i in range(n):
        s1 += a[i][i]
        s2 += a[i][n-i-1]
    return abs(s1 - s2)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    a = []

    for _ in xrange(n):
        a.append(map(int, raw_input().rstrip().split()))

    result = diagonalDifference(a)

    f.write(str(result) + '\n')

    f.close()
