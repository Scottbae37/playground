import collections
from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = collections.deque()
        q.append(root)
        depth = 0
        while q:
            depth += 1
            for _ in range(len(q)):
                r = q.popleft()
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
        return depth

