#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    new_grid = []
    for row in grid:
        new_row = "".join(sorted(list(row)))
        new_grid.append(new_row)
    
    for i in range(len(grid) - 1):
        for j in range(len(grid[0])):
            if ord(new_grid[i+1][j]) < ord(new_grid[i][j]):
                print(i, j)
                print(new_grid)
                return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
