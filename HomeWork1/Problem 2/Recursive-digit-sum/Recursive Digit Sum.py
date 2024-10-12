# Recursive Digit Sum
#!/bin/python3
import math
import os
import random
import re
import sys


def superDigit(n, k):
    initial_sum = sum(int(digit) for digit in n) * k
    return get_super_digit(initial_sum)
def get_super_digit(p):
    while p >= 10:
        p = sum(int(digit) for digit in str(p))
    return p
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = first_multiple_input[0]
    k = int(first_multiple_input[1])
    result = superDigit(n, k)
    fptr.write(str(result) + '\n')
    fptr.close()