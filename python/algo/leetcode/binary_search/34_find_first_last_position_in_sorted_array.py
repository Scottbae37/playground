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
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        def search(is_first):
            first, last = 0, len(nums) - 1
            while first <= last:
                mid = (first + last) // 2
                if nums[mid] == target:
                    if is_first:
                        if mid == first or nums[mid - 1] < target:
                            return mid
                        last = mid - 1
                    else:
                        if mid == last or nums[mid + 1] > target:
                            return mid
                        first = mid + 1
                elif nums[mid] < target:
                    first = mid + 1
                else:
                    last = mid - 1
            return -1

        ans = []
        ans.append(search(True))
        ans.append(search(False))
        return ans


if __name__ == '__main__':
    s = Solution()
    assert [3, 4] == s.searchRange([5, 7, 7, 8, 8, 10], 8)
    assert [-1, -1] == s.searchRange([5, 7, 7, 8, 8, 10], 6)
    assert [-1, -1] == s.searchRange([], 0)
    assert [2, 5] == s.searchRange([1,2,3,3,3,3,4,5,9], 3)

# class Solution:
#     def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
