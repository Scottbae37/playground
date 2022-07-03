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
    def minCost(self, costs: List[List[int]]) -> int:
        N = len(costs)
        for i in range(N - 2, -1, -1):
            costs[i][0] += min(costs[i + 1][1], costs[i + 1][2])
            costs[i][1] += min(costs[i + 1][0], costs[i + 1][2])
            costs[i][2] += min(costs[i + 1][1], costs[i + 1][0])

        return min(costs[0])


if __name__ == '__main__':
    assert 10 == Solution().minCost([[17, 2, 17], [16, 16, 5], [14, 3, 19]])
    assert 2 == Solution().minCost([[7, 6, 2]])
