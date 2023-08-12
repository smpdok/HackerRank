#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    length_of_matrix = len(matrix)
    sub_matrix_length = length_of_matrix//2
    sub_mat = []
    ## Create left quadrant sub matrix of size n * n
    for i in range(sub_matrix_length):
        sub_mat.append(matrix[i][:sub_matrix_length])
    print(sub_mat)
    s = 0
    l = length_of_matrix - 1
    ## For each element in sub matrix find the max of possible values from matrix
    for item_idx, item in enumerate(sub_mat):
        for sub_item_idx, sub_item in enumerate(item):
            s += max([matrix[item_idx][sub_item_idx], matrix[item_idx][l-sub_item_idx],
            matrix[l-item_idx][sub_item_idx], matrix[l-item_idx][l-sub_item_idx]
            ])
    return s
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
