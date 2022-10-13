def isBadVersion():
    return


class Solution:
    def firstBadVersion(self, n: int) -> int:
        ans = 0
        l, r = 1, n
        while l <= r:
            m = (l + r) // 2
            if isBadVersion(m):  # bad version 이후는 모두 bad version
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans


if __name__ == '__main__':
    cut = Solution()
