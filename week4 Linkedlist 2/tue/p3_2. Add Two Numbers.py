# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        ans = d = ListNode(99)

        push = 0
        while l1 or l2:

            d.next = ListNode(val=push)

            if l1:
                d.next.val += l1.val
                l1 = l1.next
            if l2:
                d.next.val += l2.val
                l2 = l2.next

            push = d.next.val // 10
            d.next.val = d.next.val % 10

            d = d.next

        if push != 0:
            d.next = ListNode(push)

        return ans.next