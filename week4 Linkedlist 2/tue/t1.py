class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = ListNode(
    1, ListNode(
        2, ListNode(
            2, ListNode(
                1, None))))

print(head.val)
print(head.next.val)
print(head.next.next.val)
print(head.next.next.next.val)
print(head.next.next.next.next)

head.next = head.next.next.next.next
print(head.val)
print(head.next.next)