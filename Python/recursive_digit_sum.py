#!/bin/python3

"""
https://www.hackerrank.com/challenges/one-week-preparation-kit-recursive-digit-sum/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-four
"""

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

def sum_of_digits(n, string_flag=True):
    """Return sum of digits of input

    Args:
        n (str): Input number as string
        string_flag (bool): Set to False to return integer

    Returns:
        str: sum of digits
    """
    if string_flag: 
        return str(sum([int(i) for i in list(n)]))
    return sum([int(i) for i in list(n)])

def recursive_sum(n):
    if len(n) == 1:
        return int(n)
    sum_of_num = sum_of_digits(n)
    return recursive_sum(sum_of_num)

def superDigit(n, k):
    input_number = str(sum_of_digits(n, string_flag=False)*k)
    s = recursive_sum(input_number)
    return s
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
