import collections
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        return 0


if __name__ == '__main__':
    # s = Solution()
    # actual = s.minMeetingRooms([])
    # assert 0 == actual
    # collections.defaultdict
    #
    # actual = s.minMeetingRooms([[2, 7]])
    # assert 1 == actual
    #
    # actual = s.minMeetingRooms([[7, 10], [2, 4]])
    # assert 1 == actual
    #
    # actual = s.minMeetingRooms([[5, 8], [6, 8]])
    # assert 2 == actual
    #
    # actual = s.minMeetingRooms([[0, 30], [5, 10], [15, 20]])
    # assert 2 == actual
    #
    # TC2 = [[2, 11], [6, 16], [11, 16]]
    # assert 2 == s.minMeetingRooms(TC2)
    #
    # TC3 = []
    # assert 0 == s.minMeetingRooms(TC3)
    #
    # TC4 = [[5, 8], [6, 8]]
    # assert 2 == s.minMeetingRooms(TC4)
    #
    # TC5 = [[7, 10], [2, 4]]
    # assert 1 == s.minMeetingRooms(TC5)
    #
    # input = [[4, 8] , [5, 10], [15, 20], [8, 30], [0, 50]]
    # print(s.minMeetingRooms(input))

    print("done")
    l = [1, 2, 3, 4]
    print(l[:-2][0])


# 첫 Try
# class Solution:
#     def minMeetingRooms(self, intervals: List[List[int]]) -> int:
#         if len(intervals) == 0:
#             return 0
#
#         ans = 1
#         l = sorted(intervals, key= lambda v: v[1])
#
#         end = 0
#         for m in l:
#             if m[0] < end:
#                 ans += 1
#             end = m[1]
#         return ans