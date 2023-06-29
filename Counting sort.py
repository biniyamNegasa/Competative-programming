#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr,n):
    c=[0 for _ in range(100)]
    # Write your code here
    for i in arr:
        c[i]+=1
    
    return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr,n)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
