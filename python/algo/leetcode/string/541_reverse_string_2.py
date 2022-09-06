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
    def reverseStr(self, s: str, k: int) -> str:
        end = len(s)
        cur = 0
        ans = list(s)

        def rever(i, j, s):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        while True:
            tmp = end - cur
            if tmp < k:
                rever(cur, end - 1, ans)
                break
            if k <= tmp < 2 * k:
                rever(cur, cur + k - 1, ans)
                break
            if tmp >= 2 * k:
                rever(cur, cur + k - 1, ans)
                cur = cur + 2 * k
        return str.join('', ans)


    def sol_reverseStr(self, s, k):
        a = list(s)
        for i in xrange(0, len(a), 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)


if __name__ == '__main__':
    assert "bacdfeg" == Solution().reverseStr("abcdefg", 2)
    assert "bacd" == Solution().reverseStr("abcd", 2)