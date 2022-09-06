class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0] * 128

        left = right = 0
        ans = 0
        while right < len(s):
            r = ord(s[right])
            chars[r] += 1

            while chars[r] > 1:
                l = ord(s[left])
                chars[l] -= 1
                left += 1

            ans = max(ans, right - left + 1)
            right += 1
        return ans


if __name__ == '__main__':
    assert 3 == Solution().lengthOfLongestSubstring("abcabcbb")
    assert 1 == Solution().lengthOfLongestSubstring("bbbbb")
    assert 3 == Solution().lengthOfLongestSubstring("pwwkew")
