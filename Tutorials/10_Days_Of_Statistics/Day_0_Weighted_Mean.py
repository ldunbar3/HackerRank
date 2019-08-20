# https://www.hackerrank.com/challenges/s10-weighted-mean/problem?h_r=next-challenge&h_v=zen

if __name__ == '__main__':
    n = int(input())
    elements = list(map(int, input().split()))
    weights = list(map(int, input().split()))
    print(f"{(sum([elements[i] * weights[i] for i in range(n)]) / sum(weights)):.1f}")