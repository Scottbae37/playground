from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # # 찾거나, empty이거나
        # if root == None or root.val == val:
        #     return root
        # if root.val < val:
        #     return self.searchBST(root.right, val)
        # else:
        #     return self.searchBST(root.left, val)
        # ans = None
        # tmp = root
        while root is not None and root.val != val:
            if root.val < val:
                root = root.right
            else:
                root = root.left
        return root

