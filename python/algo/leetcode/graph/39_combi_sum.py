from typing import *


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        comb = []

        def dfs(start, tmp):
            if tmp == target:
                result.append(comb[:])
                return
            if tmp > target:
                return
            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                dfs(i, candidates[i] + tmp)
                comb.pop()

        dfs(0, 0)

        return result


if __name__ == '__main__':
    assert [[2, 2, 3], [7]] == Solution().combinationSum([2, 3, 6, 7], 7)
    assert [[2, 2, 2, 2], [2, 3, 3], [3, 5]] == Solution().combinationSum([2, 3, 5], 8)
    assert [] == Solution().combinationSum([2], 1)

    l = "a,b,c,d".split(",")
    # for e in l:
    #     print(e)
    # print(l[-1])
    for i in range(len(l)):
        print(-i)
        print(l[-i])
