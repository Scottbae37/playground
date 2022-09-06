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
    def search(self, nums: List[int], target: int) -> int:
        # corner case
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            return -1

        def find_rotate_index(left, right):
            if nums[left] < nums[right]:
                return 0

            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] > nums[pivot + 1]:
                    return pivot + 1
                else:
                    if nums[pivot] < nums[left]:
                        right = pivot - 1
                    else:
                        left = pivot + 1

        left, right = 0, len(nums) - 1
        idx = find_rotate_index(left, right)

        def search(left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        ans = search(0, idx)
        if ans != -1:
            return ans
        return search(idx, len(nums) - 1)


if __name__ == '__main__':
    cut = Solution()
    assert 4 == cut.search([4, 5, 6, 7, 0, 1, 2], 0)
    assert 0 == cut.search([1], 1)
    assert -1 == cut.search([4, 5, 6, 7, 0, 1, 2], 3)
