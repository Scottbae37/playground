import collections
from typing import List


def in_range(i, j, grid: List[List[int]]) -> bool:
    if i < 0:
        return False
    if j < 0:
        return False
    if i >= len(grid):
        return False
    if j >= len(grid[0]):
        return False
    return True


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        cnt = -1
        fresh_cnt = 0
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh_cnt += 1
        if fresh_cnt == 0:
            return 0
        q.append((-1, -1))
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q:
            (i, j) = q.popleft()
            if i == -1:
                cnt += 1
                if q:
                    q.append((-1, -1))
                continue
            for each in direction:
                n_i = i + each[0]
                n_j = j + each[1]
                if in_range(n_i, n_j, grid):
                    if grid[n_i][n_j] == 1:
                        fresh_cnt -= 1
                        grid[n_i][n_j] = 2
                        q.append((n_i, n_j))
        if fresh_cnt > 0:
            return -1
        return cnt


if __name__ == '__main__':
    cut = Solution()
    assert 4 == cut.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
    assert -1 == cut.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]])
    assert 0 == cut.orangesRotting([[0, 2]])
