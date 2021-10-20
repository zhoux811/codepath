# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head.next:
            return

        if n == 0:
            return head
        """
        h2 = head


        L = 0
        while h2:
            h2 = h2.next
            L += 1
        """

        d = slow = ListNode(next=head)
        fast = head

        for _ in range(n):
            fast = fast.next

        if not fast:
            slow.next = slow.next.next
        else:
            while fast:
                fast = fast.next
                slow = slow.next
            slow.next = slow.next.next

        return d.next