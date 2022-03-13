from enum import Enum
from typing import List


class Direction(Enum):
    R = 1
    D = 2
    L = 3
    U = 4


def in_range(row, col, matrix) -> bool:
    if row < 0:
        return False
    if col < 0:
        return False
    if row >= len(matrix):
        return False
    if col >= len(matrix[0]):
        return False
    return True


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 총 칸이 채워질 때까지 loop
        # OutOfRange || visit을 만나면 방향 전환
        # 방향은 우 하 좌 상
        ans = []
        until = len(matrix) * len(matrix[0])
        visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
        dire = Direction.R
        row = col = 0
        total = 0
        while until > total:
            if not visited[row][col]:
                visited[row][col] = True
                ans.append(matrix[row][col])
                total += 1
            if dire == Direction.R:
                dire = Direction.D
                while True:
                    n_col = col + 1
                    if not in_range(row, n_col, matrix) or visited[row][n_col]:
                        break
                    visited[row][n_col] = True
                    ans.append(matrix[row][n_col])
                    col = n_col
                    total += 1
            elif dire == Direction.D:
                dire = Direction.L
                while True:
                    n_row = row + 1
                    if not in_range(n_row, col, matrix) or visited[n_row][col]:
                        break
                    visited[n_row][col] = True
                    ans.append(matrix[n_row][col])
                    row = n_row
                    total += 1
            elif dire == Direction.L:
                dire = Direction.U
                while True:
                    n_col = col - 1
                    if not in_range(row, n_col, matrix) or visited[row][n_col]:
                        break
                    visited[row][n_col] = True
                    ans.append(matrix[row][n_col])
                    col = n_col
                    total += 1
            else:
                dire = Direction.R
                while True:
                    n_row = row - 1
                    if not in_range(n_row, col, matrix) or visited[n_row][col]:
                        break
                    visited[n_row][col] = True
                    ans.append(matrix[n_row][col])
                    row = n_row
                    total += 1
        return ans


if __name__ == '__main__':
    cut = Solution()
    assert [1, 2, 3, 6, 9, 8, 7, 4, 5] == cut.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7] == cut.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
