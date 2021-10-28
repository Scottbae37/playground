# https://www.acmicpc.net/problem/11053
# LIS(Longest Increasing Sequence)

# 6
# 10 20 10 30 20 50

# 4

# 6
# 10 20 11 12 13 14
# 5

if __name__ == '__main__':
    n = int(input())
    l = list(map(int, input().split()))

    ans = 0
    for i in range(0, n):
        cur = l[i]
        tmp = 1
        for j in range(i+1, n):
            if cur < l[j]:
                cur = l[j]
                tmp += 1
        ans = max(ans, tmp)
    print(ans)
