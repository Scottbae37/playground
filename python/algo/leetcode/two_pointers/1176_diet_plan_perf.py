from typing import *


class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        ans = 0
        s, e = 0, k - 1
        t = sum(calories[s:k])
        while True:
            if t < lower:
                ans -= 1
            if t > upper:
                ans += 1
            t -= calories[s]
            s += 1
            e += 1
            if e == len(calories):
                break
            t += calories[e]
        return ans


if __name__ == '__main__':
    cut = Solution()
    assert 0 == cut.dietPlanPerformance([1, 2, 3, 4, 5], 1, 3, 3)
    assert 1 == cut.dietPlanPerformance([3, 2], 2, 0, 1)
    assert 0 == cut.dietPlanPerformance([6, 5, 0, 0], 2, 1, 5)

