# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        d = dict()

        h3 = h2 = ListNode(next=head)

        while head:
            if head.val in d:
                d[head.val] += 1
            else:
                d[head.val] = 1
            head = head.next

        while h2.next:
            if d[h2.next.val] != 1:
                h2.next = h2.next.next
            else:
                h2 = h2.next

        return h3.next