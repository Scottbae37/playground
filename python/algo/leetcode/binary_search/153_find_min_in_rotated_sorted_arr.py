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
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if nums[l] <= nums[r]:
            return nums[l]
        while l <= r:
            m = (l + r) // 2
            if nums[m] > nums[m + 1]:
                return nums[m + 1]
            else:
                if nums[m] < nums[l]:
                    r = m - 1
                else:
                    l = m + 1

        return nums[l]


if __name__ == '__main__':
    cut = Solution()
    assert 1 == cut.findMin([1])
    assert 1 == cut.findMin([3, 1, 2])
    assert 1 == cut.findMin([2, 3, 4, 5, 1])
    assert 1 == cut.findMin([3, 4, 5, 1, 2])
    assert 0 == cut.findMin([4, 5, 6, 7, 0, 1, 2])
    assert 11 == cut.findMin([11, 13, 15, 17])
