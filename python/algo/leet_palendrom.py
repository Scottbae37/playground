# 7
# 1 2 1 3 1 2 1
# 4
# 1 3
# 2 5
# 3 3
# 5 7
def go(i, j):
    global l, dp
    if i == j:
        dp[i][j] = True
        return True
    if i+1 == j:
        if l[i] == l[j]:
            dp[i][j] = True
            return True
        return False
    if dp[i][j]:
        return dp[i][j]
    if l[i] != l[j]:
        dp[i][j] = False
        return dp[i][j]
    dp[i][j] = go(i + 1, j - 1)
    return dp[i][j]

if __name__ == '__main__':
    input()
    l = list(map(int, input().split()))
    n = int(input())
    dp = [[False] * len(l) for _ in range(len(l))]
    go(0, len(l)-1)
    for _ in range(n):
        i, j = map(int, input().split())
        print(i, j)
        print(dp[i-1][j-1])