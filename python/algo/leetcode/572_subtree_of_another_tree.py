# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def pre_order(root: Optional[TreeNode], l):
    if root:
        l.append(root.val)
        pre_order(root.left, l)
        pre_order(root.right, l)


def find_same_root(root: Optional[TreeNode], target):
    if root:
        if target == root.val:
            return root
        return find_same_root(root.left, target)
        return find_same_root(root.right, target)


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        l = []
        pre_order(subRoot, l)
        print(l)
        an = find_same_root(root, subRoot.val)
        if not an:
            return False
        l2 = []
        pre_order(an, l2)
        print(l2)
        return l == l2