# https://www.hackerrank.com/challenges/30-review-loop/problem

if __name__ == '__main__':

    N = int(input())
    for i in range(0, N):
        string = input()
        evens = []
        odds = []
        for k, v in enumerate(string):
            if k == 0 or k % 2 == 0:
                evens.append(v)
            else:
                odds.append(v)
        print(f"{''.join(evens)} {''.join(odds)}")