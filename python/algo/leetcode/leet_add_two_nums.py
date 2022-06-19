# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = self.to_reverse_list(l1)
        list2 = self.to_reverse_list(l2)

        sums = []
        carry = 0
        while len(list1) > 0 or len(list2) > 0:
            v1, v2 = 0, 0
            if len(list1) > 0:
                v1 = list1.pop()
            if len(list2) > 0:
                v2 = list2.pop()
            sums.append((v1 + v2 + carry) % 10)
            carry = int((v1 + v2 + carry)/10)
        if carry:
            sums.append(carry)

        return self.to_list_node(sums)

    def to_reverse_list(self, root_node):
        l = []
        tmp = root_node
        l.append(tmp.val)
        while tmp.next:
            tmp = tmp.next
            l.append(tmp.val)
        l.reverse()
        return l

    def to_list_node(self, sums):
        ans = ListNode(sums[-1])
        for v in sums[-2::-1]:
            ans = ListNode(v, ans)
        return ans


if __name__ == '__main__':
    # ListNode(9, ListNode(4, ListNode(2)))
    # ListNode(9, ListNode(4, ListNode(6, ListNode(5))))

    actual = Solution().addTwoNumbers(ListNode(9, ListNode(4, ListNode(2))),
                                       ListNode(9, ListNode(4, ListNode(6, ListNode(5)))))
    print(actual)
    # correct: [7,0,4,0,1]
    # wrong: [8,9,8,5]
# [2,4,9]
# [5,6,4,9]


