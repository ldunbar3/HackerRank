#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(num):
    return 1 if num == 1 else factorial(num - 1) * num

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    result = factorial(n)
    fptr.write(str(result) + '\n')
    fptr.close()