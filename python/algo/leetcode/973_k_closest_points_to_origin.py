import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for i in range(len(points)):
            point = points[i]
            x = point[0]
            y = point[1]
            distances.append((i, math.sqrt(x*x + y*y)))
        sorted_distances = sorted(distances, key=lambda v: v[1])
        ans = []
        for i in range(k):
            ans.append(points[sorted_distances[i][0]])
        return ans