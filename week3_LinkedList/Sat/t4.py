class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = ListNode(
    1, ListNode(
        2, ListNode(
            2, ListNode(
                1, None))))

while head:
    print(head.val)
    head = head.next

dummy = ListNode(next=head)
print(dummy.val)
