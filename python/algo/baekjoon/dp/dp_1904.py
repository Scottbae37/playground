# https://www.acmicpc.net/problem/1904

# N이 1,000,000 이므로 O(N)을 통해서 풀어야함

# 4
# 5
if __name__ == '__main__':
    n = int(input())
    dp = [0] * 1000001
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = (dp[i - 2] + dp[i - 1]) % 15746
    print(dp[n])
