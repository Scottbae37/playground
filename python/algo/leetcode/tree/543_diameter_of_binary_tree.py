from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter: int = 0
        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)

            self.diameter = max(self.diameter, left + right + 2)
            return max(left, right) + 1

        dfs(root)
        return self.diameter

# 직격을 구하는게, 왼쪽 가장 깊은 node와 오른쪽 가장 깊은 node + 1(root포함)
