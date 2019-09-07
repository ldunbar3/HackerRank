# https://www.hackerrank.com/challenges/30-binary-numbers/problem

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    binary = list(bin(n)[2:])

    count = 0
    max_count = 0

    for i in binary:
        if (i == '1'):
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0
    if count > max_count:
        max_count = count
    print (max_count)