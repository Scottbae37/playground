import sys
from typing import *


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 0보다 작으면 버리고, #크면 우측을 증가
        # 언제까지? s가 end와 같아 질때 까지
        ans = -sys.maxsize
        e = 0
        total = 0
        while e < len(nums):
            total += nums[e]
            if total <= 0:
                total = 0
            e += 1
            ans = max(ans, total)
        if ans == 0:
            return max(nums)
        return ans


if __name__ == '__main__':
    s = Solution()
    
