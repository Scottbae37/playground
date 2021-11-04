# https://www.acmicpc.net/problem/11053
# LIS(Longest Increasing Sequence)
# N^2
# D[i]= array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
# D[i] = max(D[i], D[j]+1) if array[j] < array[i]

# 6
# 10 20 10 30 20 50

# 4

# 6
# 10 20 11 12 13 14
# 5

if __name__ == '__main__':
    n = int(input())
    l = list(map(int, input().split()))

    dp = [1] * n


    print(max(dp))
    # 6
    # 10 20 11 12 13 14
    # 5
    # 이전 의 진행된 애보다 내가 작다면 continue
    # 이전의 진행된 애보다 내가 크다면, max(이전의 애+1, 나의 이전값)
    # dp = [1]*n
    # for i in range(1, n):
    #     for j in range(0, i):
    #         if l[j] < l[i]:
    #             dp[i] = max(dp[i], dp[j] + 1)
    #
    # print(max(dp))
