from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        pos = 0
        end = len(nums) - 1
        cnt = 0
        jump = 0
        while True:
            cnt += 1
            jump = nums[pos]
            if pos + jump >= end:
                break
            for i in range(pos + 1, pos + jump + 1):
                reach = i + nums[i]
                if reach > max_jump:
                    max_jump = reach
                    nextpos = i
            pos = nextpos
        return cnt


def fun(nums: List[int]):
    pos = 0
    numjump = 0
    while pos < len(nums) - 1:
        numjump += 1
        curjump = nums[pos]
        if pos + curjump >= len(nums) - 1:
            break
        maxreach = 0
        nextpos = 0
        for i in range(pos + 1, pos + curjump + 1):
            reach = i + nums[i]
            if reach > maxreach:
                maxreach = reach
                nextpos = i
        pos = nextpos
    return numjump


if __name__ == '__main__':
    # actual = Solution().jump([1,2,0,1])
    # assert 2 == actual
    actual = Solution().jump([2, 3, 1, 1, 4])
    # actual = fun([2, 3, 1, 1, 4])
    assert 2 == actual
