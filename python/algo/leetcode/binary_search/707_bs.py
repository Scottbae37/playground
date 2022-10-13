from typing import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1


if __name__ == '__main__':
    cut = Solution()
    assert 4 == cut.search([-1, 0, 3, 5, 9, 12], 9)
    assert -1 == cut.search([-1, 0, 3, 5, 9, 12], 2)
