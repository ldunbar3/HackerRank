# https://www.hackerrank.com/challenges/30-arrays/problem

'''
Print the elements of array A in reverse order as a single line of space-separated numbers
'''

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    for i in arr[::-1]:
        print(f"{i} ", end="")