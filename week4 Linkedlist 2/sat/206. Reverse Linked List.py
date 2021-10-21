# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr is not None:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n
        head = prev

        return prev

    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return r

        n = head.next
        head.next = r

        return self.reverseList2(n, head)
