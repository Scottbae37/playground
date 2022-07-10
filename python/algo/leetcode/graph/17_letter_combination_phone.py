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
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        def dfs(idx, path):
            if len(path) == len(digits):
                result.append(path)
                return
            for i in range(idx, len(digits)):
                for c in dials[digits[i]]:
                    dfs(i + 1, path + c)

        dials = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                 '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        result = []
        dfs(0, '')

        return result


if __name__ == '__main__':
    assert ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"] == Solution().letterCombinations("23")
