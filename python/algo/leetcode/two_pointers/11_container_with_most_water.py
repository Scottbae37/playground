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
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        ans = 0
        while left < right:
            ans = max(ans, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans


if __name__ == '__main__':
    cut = Solution()
    assert 49 == cut.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    assert 1 == cut.maxArea([1, 1])
