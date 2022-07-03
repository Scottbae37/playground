import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

class Solution:
    def rob(self, nums: List[int]) -> int:
        # 맨 뒤에서, 먹는것과, 먹지 않았을 때 큰거로 세팅
        dp = collections.defaultdict(int)
        
        dp[len(nums)-1] = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            dp[i] = max(dp[i+1], dp[i+2] + nums[i])
        return dp[0]


def sol2(nums: List[int]) -> int:
    if not nums:
        return 0

    N = len(nums)
    next_rob = nums[-1]
    next_next_rob = 0

    for i in range(N - 2, -1, -1):
        cur = max(next_rob, next_next_rob + nums[i])
        next_next_rob = next_rob
        next_rob = cur
    return next_rob


if __name__ == '__main__':
    assert 4 == Solution().rob([1, 2, 3, 1])
    assert 12 == sol2([2, 7, 9, 3, 1])
