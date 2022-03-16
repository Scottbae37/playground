def search_palindrome(s, start, end):
    while start >= 0 and end < len(s) and s[start] == s[end]:
        start -= 1
        end += 1
    return s[start + 1:end]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            ret = search_palindrome(s, i, i)
            if len(ret) > len(ans):
                ans = ret
            ret = search_palindrome(s, i, i + 1)
            if len(ret) > len(ans):
                ans = ret
        return ans
