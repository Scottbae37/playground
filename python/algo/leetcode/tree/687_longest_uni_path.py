from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_val: int = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            if root.left and root.left.val == root.val:
                left += 1
            else:
                left = 0
            if root.right and root.right.val == root.val:
                right += 1
            else:
                right = 0
            self.max_val = max(self.max_val, left + right)
            return max(left, right)

        dfs(root)
        return self.max_val

# 트리의 지름을 구하는 것에서 부모와 같은지 비교하는 부분이 추가됨
# return max(left, right)에서 체크 해야 할 부분은, 현재 노드에서는 left, right를 다 선택할 수 있지만(left+right) 현재 노드의 부모 노드에서는 짐금의 양쪽 자식 노들르 동시에 연결할 수 없다.
# 단방향이므로 양쪽 자식 노드 중 어느 한쪽 자식만 택할 수 있으며, 이는 트리의 특징이기도 하다. 따라서 둘 중 큰 값을 상태값으로 리턴해준다. 어차피 한 군데만 방문할 수 있다면 더 큰 쪽을 방문