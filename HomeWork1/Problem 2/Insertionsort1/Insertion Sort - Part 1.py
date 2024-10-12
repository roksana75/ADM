# Insertion Sort - Part 1
#!/bin/python3
import math
import os
import random
import re
import sys
def insertionSort1(n, arr):
    last_elmnt = arr[-1]
    i = n - 2
    while i >= 0 and arr[i] > last_elmnt:
        arr[i + 1] = arr[i]
        print(" ".join(map(str, arr)))
        i -= 1
    arr[i + 1] = last_elmnt
    print(" ".join(map(str, arr)))
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)
