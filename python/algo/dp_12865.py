# Knapsack Problem
# O(NK)

# https://www.acmicpc.net/problem/12865

# 4 7
# 6 13
# 4 8
# 3 6
# 5 12

# 14

if __name__ == '__main__':
    # 무게k를 단계적으로 늘려가며, 넣을 수 있는 최대치를 구한다
    # 안들어가는 무게라면 가장 이전 값을 그대로 저장
    # 들어가는 무게라면 max(현재 위치 이전 무게:그 동안 최대, 나의 무게- 현재 무게 한 곳에서 + 현재 가치)
    n, k = map(int, input().split())
    k += 1
    dp = [[0]*k for _ in range(n+1)]
    for i in range(1, n+1):
        weight, value = map(int, input().split())
        for j in range(1, k):
            if weight > j:
                dp[i][j] = dp[i-1][j]
                continue
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - weight] + value)
    print(dp[n][k-1])
