# https://www.hackerrank.com/challenges/s10-basic-statistics/problem

'''
Task
Given an array, , of integers, calculate and print the respective mean, median, and 
mode on separate lines. If your array contains more than one modal value, choose 
the numerically smallest one.
'''

import queue as Q
import collections

if __name__ == '__main__':
    n = int(input())
    a = sorted(list(map(int, input().split())))

    # MEAN
    print(f"{(sum(a) / len(a)):.1f}")

    # MEDIAN
    mid = n // 2
    if n % 2 == 0:
        median = (a[mid-1] + a[mid]) / 2
    else:
        median = a[mid]
    print(f"{median:.1f}")

    # MODE
    count_map = collections.Counter(a)
    q = Q.PriorityQueue()
    for pair in count_map.items():
        q.put((-pair[1], pair[0]))

    print(q.get()[1])