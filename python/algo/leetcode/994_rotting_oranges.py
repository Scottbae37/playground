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
        n = len(grid)
        m = len(grid[0])
        visit = [[False] * m for _ in range(n)]

        ans = 0
        q = collections.deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j))
                    visit[i][j] = True

        def in_range(i, j):
            if i < 0:
                return False
            if j < 0:
                return False
            if i == n:
                return False
            if j == m:
                return False
            if grid[i][j] == 0 or 2 == grid[i][j]:
                return False
            return True

        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q:
            ans += 1
            for _ in range(len(q)):
                (i, j) = q.popleft()
                visit[i][j] = True
                for each in direction:
                    n_i = i + each[0]
                    n_j = j + each[1]
                    if in_range(n_i, n_j) and not visit[n_i][n_j]:
                        grid[n_i][n_j] = 2
                        q.append((n_i, n_j))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        if ans >= 1:
            return ans - 1
        return ans


if __name__ == '__main__':
    cut = Solution()
    assert 4 == cut.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
    assert -1 == cut.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]])
    assert 0 == cut.orangesRotting([[0, 2]])
    c = collections.Counter(['b', 'b', 'c'])
    print(c.most_common(len(c)))
