#!/bin/python3

"""
https://www.hackerrank.com/challenges/one-week-preparation-kit-grid-challenge/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-four
"""


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

def sort_grid_asc(grid):
    updated_grid = []
    for item in grid:
        sorted_item = "".join(sorted(list(item)))
        updated_grid.append(sorted_item)
    return updated_grid
        
        

def gridChallenge(grid):
    print("grid", grid)
    ## Sort the each element in grid in ascending order
    updated_grid = sort_grid_asc(grid)
    print("updated_grid", updated_grid)
    
    no_of_columns = len(updated_grid[0])
    print("no_of_columns", no_of_columns)
    ## Get the values of each column and check if it is sorted
    for col_idx in range(no_of_columns):
        cols = [updated_grid[row_idx][col_idx] for row_idx in range(len(updated_grid))]
        print("cols", cols)
        ## Return "NO" right away when failed.
        if cols != sorted(cols):
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
