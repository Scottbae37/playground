import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

# Ring형태로 연결된 집을 털어, 가장 많은 금액을 털 수 있는 값
# 제약: 인접한 집은 털 수 없다

class Solution:
    def rob(self, nums: List[int]) -> int:
        da = collections.defaultdict(int)
        db = collections.defaultdict(int)
        na = nums[:-1]
        nb = nums[1:]

        da[len(na)-1] = na[-1]
        db[len(nb)-1] = nb[-1]
        for i in range(len(na)-2, -1, -1):
            # 이전 것을 먹는 것이 좋았는지, 나와 건더 뛴 것을 먹는 것이 좋았는지
            da[i] = max(na[i] + da[i+2], da[i+1])
            db[i] = max(nb[i] + db[i + 2], db[i + 1])
        return max(da[0], db[0])


if __name__ == '__main__':
    assert 4 == Solution().rob([1, 2, 3, 1])
    assert 3 == Solution().rob([1, 2, 3])
