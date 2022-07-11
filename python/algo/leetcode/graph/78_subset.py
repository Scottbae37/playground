from typing import *


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        result.append([])
        sub = []

        def dfs(start, length):
            if length == len(sub):
                result.append(sub[:])
                return
            for i in range(start, len(nums)):
                sub.append(nums[i])
                dfs(i + 1, length)
                sub.pop()

        for i in range(1, len(nums) + 1):
            dfs(0, i)

        return result


if __name__ == '__main__':
    assert [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]].sort() == Solution().subsets([1, 2, 3]).sort()
    assert [[], [0]].sort() == Solution().subsets([0]).sort()
