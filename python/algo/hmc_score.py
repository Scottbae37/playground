# 5 3
# 10 50 20 70 100
# 1 3
# 3 4
# 1 5

# 26.67
# 45.00
# 50.00

if __name__ == '__main__':
    N, M = map(int, input().split())
    l = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())
        ans = sum(l[i - 1:j]) / abs(i - 1 - j)
        print(format(round(ans, 2), ".2f"))
