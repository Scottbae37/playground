from typing import *


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 0보다 크다는 것은 어찌되었건, 도움이 된다는 뜻
        ans = 0
        total = 0
        for num in nums:
            total += num
            if total < 0:
                total = 0
            ans = max(ans, total)
        if ans == 0:
            return max(nums)
        return ans


if __name__ == '__main__':
    cut = Solution()
    assert 6 == cut.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    assert 1 == cut.maxSubArray([1])
    assert 23 == cut.maxSubArray([5, 4, -1, 7, 8])
    assert -1 == cut.maxSubArray([-1])
    assert -1 == cut.maxSubArray([-1, -2])
