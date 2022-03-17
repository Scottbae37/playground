from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pre_order(root: Optional[TreeNode], l: List[int]):
    if root:
        l.append(root.val)
        pre_order(root.left, l)
        pre_order(root.right, l)


class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        l1 = []
        l2 = []
        pre_order(root1, l1)
        pre_order(root2, l2)
        # N * M
        for each1 in l1:
            for each2 in l2:
                if each1 + each2 == target:
                    return True
        return False


if __name__ == '__main__':
    cut = Solution()
    root1 = TreeNode(2, TreeNode(1), TreeNode(4))
    root2 = TreeNode(1, TreeNode(0), TreeNode(3))
    assert cut.twoSumBSTs(root1, root2, 5) is True
    root1 = TreeNode(0, TreeNode(-10), TreeNode(10))
    root2 = TreeNode(5, TreeNode(1, TreeNode(0), TreeNode(2)), TreeNode(7))
    assert cut.twoSumBSTs(root1, root2, 18) is not True
