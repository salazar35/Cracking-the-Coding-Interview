#!/bin/python

from __future__ import print_function
from __future__ import division

import os
import sys

#
# Complete the plusMinus function below.
#
def plusMinus(arr):
    #
    # Write your code here.
    #
    n = len(arr)
    pos = neg = zer = 0
    for x in arr:
        if x > 0:
            pos += 1
        elif x < 0:
            neg += 1
        else:
            zer += 1
    print("%.6f" % float(pos/n))
    print("%.6f" % float(neg/n))
    print("%.6f" % float(zer/n))

if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    plusMinus(arr)
