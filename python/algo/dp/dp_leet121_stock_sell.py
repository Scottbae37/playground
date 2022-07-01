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
    def maxProfit(self, prices: List[int]) -> int:
        # 꺽이는 점을 찾을 필요 없음
        # 해결법: min이 갱신 될때마다, max값 업데이트
        min_val = 10001
        max_val = 0

        for price in prices:
            min_val = min(min_val, price)
            max_val = max(max_val, price - min_val)
        return max_val


if __name__ == '__main__':
    assert 5 == Solution().maxProfit([7, 1, 5, 3, 6, 4])
    assert 0 == Solution().maxProfit([7, 6, 4, 3, 1])
