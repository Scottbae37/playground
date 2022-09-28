from typing import List


class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        # Sliding windows
        ans = 0
        left = 0
        right = k
        tmp = sum(calories[left:right])
        while right < len(calories):
            if tmp < lower:
                ans -= 1
            elif tmp > upper:
                ans += 1
            tmp -= calories[left]
            tmp += calories[right]
            left += 1
            right += 1
        if tmp < lower:
            ans -= 1
        elif tmp > upper:
            ans += 1
        return ans

if __name__ == '__main__':
    print('a')