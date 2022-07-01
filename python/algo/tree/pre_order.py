from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pre_order(root: Optional[TreeNode], l):
    if root:
        l.append(root.val)
        pre_order(root.left, l)
        pre_order(root.right, l)
