from typing import *
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 자식을 뒤집고, 자식을 큐에 넣고
        # BFS로
        q = collections.deque([root])
        q.append(root)
        while q:
            t = q.popleft()
            if t:
                t.left, t.right = t.right, t.left
                q.append(t.left)
                q.append(t.right)
        return root


if __name__ == '__main__':
    assert [2, 3, 1] == Solution().invertTree([2, 1, 3])
    assert [4, 7, 2, 9, 6, 3, 1] == Solution().invertTree([4, 2, 7, 1, 3, 6, 9])
