# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        """
        nset = set()

        if not head:
            return

        if not head.next:
            return head



        o = head

        nset.add(head.val)

        while head.next :

            if head.next.val not in nset:
                nset.add(head.next.val)
                head = head.next
            else:
                head.next = head.next.next
        return o
        """

        o = head

        if not head:
            return

        if not head.next:
            return head

        while head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return o