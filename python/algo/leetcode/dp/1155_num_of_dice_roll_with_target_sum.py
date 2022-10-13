class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10 ** 9 + 7
        dp = {}

        def recur(n, total):
            if total < 0:
                return 0
            if n == 0:
                if total == target:
                    return 1
                return 0
            if (n, total) in dp:
                return dp[(n, total)]
            ret = 0
            for i in range(1, k + 1):
                ret += recur(n - 1, total + i)
            dp[(n, total)] = ret
            return ret

        return recur(n, 0) % mod


if __name__ == '__main__':
    cut = Solution()
    assert 1 == cut.numRollsToTarget(1, 6, 3)
    assert 6 == cut.numRollsToTarget(2, 6, 7)
    assert 222616187 == cut.numRollsToTarget(30, 30, 500)



