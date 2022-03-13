class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # 괄호의 idx와 타입을 stack에 넣어서 valid하지 않은 괄호idx 삭제
        idx_to_remove = set()
        stack = []
        for i, c in enumerate(s):
            if c not in "()":
                continue
            if c == "(":
                stack.append(i)
                continue
            if not stack:
                idx_to_remove.add(i)
                continue
            stack.pop()
        idx_to_remove = idx_to_remove.union(set(stack))
        print(idx_to_remove)
        ans = []
        for i, c in enumerate(s):
            if i not in idx_to_remove:
                ans.append(c)
        return "".join(ans)


if __name__ == '__main__':
    cut = Solution()
    assert "" == cut.minRemoveToMakeValid("))((")
    assert "ab(c)d", cut.minRemoveToMakeValid("a)b(c)d")
    assert "lee(t(c)o)de" == cut.minRemoveToMakeValid("lee(t(c)o)de)")
