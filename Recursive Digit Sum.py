#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def sumDigit(string):
    sum = 0
    for i in range(len(string)):
        sum += int(string[i])
    return sum

def superDigit(n, k):
    # Write your code here
    s = str(sumDigit(n) * k)
    
    while True:
        x = sumDigit(s)
        if x < 10:
            return x
        else:
            s = str(x)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
