import typing

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 다음이 가르치는걸 이전 것을 가르치도록 방향 뒤집기

        # 1) Interation
        # prev = None
        # cur = head
        # while cur:
        #     next_tmp = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = next_tmp
        # return prev

        # 2) Recursion
        if not head:
            return head
        if not head.next:
            return head
        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node