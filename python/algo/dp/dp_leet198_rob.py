import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

m = 0

def sol(accu, idx, nums, take):
    global m
    if idx == len(nums):
        m = max(accu, m)
        return

    if take:
        accu += nums[idx]
    sol(accu, idx + 1, nums, False)
    sol(accu, idx + 1, nums, True)


class Solution:
    def rob(self, nums: List[int]) -> int:
        # take or not take
        # sum이 커지는
        dp = []
        sol(0, 0, nums, True)
        sol(0, 0, nums, False)
        print(m)


if __name__ == '__main__':
    assert 4 == Solution().rob([1, 2, 3, 1])
    # assert 12 == Solution().rob([2, 7, 9, 3, 1])
