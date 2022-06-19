import copy
from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        ll = []
        for i in range(n):
            tmp = [0, 0, 0, 0, 0, 0, 0, 0]
            for j in range(1, 7):
                if cells[j - 1] == cells[j + 1]:
                    tmp[j] = 1
                else:
                    tmp[j] = 0

            if tmp in ll:
                idx = (n % len(ll)) - 1
                return ll[idx]
            ll.append(copy.deepcopy(tmp))
            cells = tmp
        return cells


if __name__ == '__main__':
    assert [0, 0, 1, 1, 0, 0, 0, 0] == Solution().prisonAfterNDays([0, 1, 0, 1, 1, 0, 0, 1], 7)
    assert [0, 0, 1, 1, 1, 1, 1, 0] == Solution().prisonAfterNDays([1, 0, 0, 1, 0, 0, 1, 0], 1000000000)

