dp = {0: 0, 1: 1}


class Solution:
    def fib(self, n: int) -> int:
        # Recursion
        # 2^n, every call makes 2 calls

        if n <= 1:

        # bottom up

        # dp = collections.defaultdict(int)
        # dp[0] = 0
        # dp[1] = 1
        # for i in range(2, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]

        # top-down

        # if n in dp:
        #     return dp[n]
        # dp[n] = self.fib(n-1) + self.fib(n-2)
        # return dp[n]


if __name__ == '__main__':
    assert 4 == Solution().fib(3)
    assert 3 == Solution().fib(2)



