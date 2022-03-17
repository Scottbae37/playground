import sys

sys.setrecursionlimit(15000)


def recursive(n, num_face, target):
    global dp
    if n == 0:
        if 0 == target:
            return 1
        return 0

    if (n, target) in dp:
        return dp[(n, target)]

    ret = 0
    for i in range(1, num_face + 1):
        ret += recursive(n - 1, num_face, target - i)
    dp[(n, target)] = ret

    return ret % (10 ** 9 + 7)


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        global dp
        dp = {}
        return recursive(n, k, target)


if __name__ == '__main__':
    cut = Solution()
    assert cut.numRollsToTarget(1, 6, 3) == 1
    assert cut.numRollsToTarget(2, 6, 7) == 6
    assert cut.numRollsToTarget(30, 30, 500) == 222616187
