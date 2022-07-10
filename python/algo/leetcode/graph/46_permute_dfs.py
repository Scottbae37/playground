import itertools
from typing import *


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(elem):
            if len(elem) == 0:
                result.append(prev[:])
            for e in elem:
                next_elem = elem[:]
                next_elem.remove(e)

                prev.append(e)
                dfs(next_elem)
                prev.pop()

        result = []
        prev = []
        dfs(nums)

        return result


class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))



if __name__ == '__main__':
    assert [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]] == Solution().permute([1, 2, 3])
    assert [[0, 1], [1, 0]] == Solution().permute([0, 1])
    assert [[1]] == Solution().permute([1])

    assert [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]] == Solution2().permute([1, 2, 3])
