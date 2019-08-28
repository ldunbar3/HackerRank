# https://www.hackerrank.com/challenges/s10-quartiles/problem

'''
Task
Given an array, ,x of n integers, calculate the respective first quartile (Q1), second quartile (Q2), and third quartile (Q3). 
It is guaranteed that Q1, Q2, and Q3 are integers.
'''
if __name__ == '__main__':
    n = int(input())
    x = sorted(list(map(int, input().split())))
    mid = n // 2
    if n % 2 == 0:
        median = (x[mid-1] + x[mid]) / 2
    else:
        median = x[mid]
    print(f"{median:.1f}")