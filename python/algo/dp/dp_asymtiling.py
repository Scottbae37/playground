# 입력
# 3
# 2
# 4
# 92

# 출력

# 0
# 2
# 913227494

dp = [0] * 101
MOD = 1000000007


def sol(n):
    if n <= 1:
        return 1
    if n <= 2:
        return 2
    if dp[n]:
        return dp[n]
    dp[n] = (sol(n - 1) + sol(n - 2)) % MOD
    return dp[n]


def asy(n):
    if (n % 2 == 1):
        return (sol(n) - sol(int(n / 2)) + MOD) % MOD
    ret = sol(n)
    ret = (ret - sol(int(n / 2)) + MOD) % MOD
    ret = (ret - sol(int(n / 2) - 1) + MOD) % MOD
    return int(ret)


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        c = int(input())
        print(asy(c))
