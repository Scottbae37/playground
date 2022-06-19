import collections
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # N번 돌고 카운팅
        # visit check
        # 뒤에껄로 찍기
        d = collections.defaultdict(int)
        visit = {}
        for v in arr1:
            d[v] += 1
            visit[v] = False

        ans = []
        for v in arr2:
            visit[v] = True
            for _ in range(d[v]):
                ans.append(v)

        l = []
        for k, v in visit.items():
            if not v:
                l.append((k, d[k]))
        l.sort(key=lambda v: v[0])
        for (k, cnt) in l:
            for _ in range(cnt):
                ans.append(k)
        return ans