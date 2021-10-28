# Knapsack Problem
# O(NK)

# https://www.acmicpc.net/problem/12865

# 4 7
# 6 13
# 4 8
# 3 6
# 5 12
#
# 14

if __name__ == '__main__':
    n, k = map(int, input().split())

    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        # 무게를 늘려가면서, 넣을 수 없을 때는 이전 값이 그대로 내려옴
        # 넣을 수 있는 무게라면, 지금 넣는게 이득일지 아니면 (무게-본인무게)가 더 이득이었는지 검색하여 업데이트
        # 그러면 답은 최종 뒤에 있는 값
        (weight, value) = map(int, input().split())
        for j in range(1, k + 1):
            if j < weight:
                dp[i][j] = dp[i-1][j]
                continue
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - weight] + value)
        # (weight, value) = map(int, input().split())
        # for j in range(1, k + 1):
        #     if j < weight:
        #         dp[i][j] = dp[i-1][j]
        #         continue
        #     dp[i][j] = max(dp[i-1][j], dp[i-1][j - weight] + value)

    # 넣을 수 없을때는 이전의 값을 그대로 쓰고
    # 넣을 수 있는 무게라면 이전의 값(자신보다 무게가 적은 애들)과 현재 값 중 max로 갱신
    # dp = [[0] * (k + 1) for _ in range(n + 1)]
    #
    # for i in range(1, n + 1):
    #     (weight, value) = map(int, input().split())
    #     for j in range(1, k + 1):
    #         # 넣을 수 없을때는 이전의 값을 그대로 쓰고
    #         # 넣을 수 있는 무게라면 이전의 값(자신보다 무게가 적은 애들)과 현재 값 중 max로 갱신
    #         if j < weight:
    #             dp[i][j] = dp[i - 1][j]
    #         else:
    #             dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
    for each in dp:
        print(each)
    print(dp[n][k])
    # # 모든 무게에 대해서 최대 가치 저장하기
