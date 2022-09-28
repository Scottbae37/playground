from typing import *


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def recur(r, c):
            if r == 0 or c == 0 or r == c:
                return 1
            return recur(r - 1, c - 1) + recur(r - 1, c)

        ans = []
        for i in range(rowIndex + 1):
            ans.append(recur(rowIndex, i))
        return ans


if __name__ == '__main__':
    cut = Solution()
    print(cut.getRow(3))
