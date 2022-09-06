import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *


def in_range(row, col, m) -> bool:
    if row < 0:
        return False
    if col < 0:
        return False
    if row >= len(m):
        return False
    if col >= len(m[0]):
        return False
    return True


directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def dfs(row, col, grid):
    for direction in directions:
        n_row = row + direction[0]
        n_col = col + direction[1]
        if in_range(n_row, n_col, grid) and grid[n_row][n_col] == "1":
            grid[n_row][n_col] = "0"
            dfs(n_row, n_col, grid)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 순회하면서 1이면 dsf 판다 0으로 바꿔 버린다
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    grid[row][col] = "0"
                    dfs(row, col, grid)
                    ans += 1
        return ans