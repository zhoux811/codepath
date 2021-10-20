class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = ListNode(
    1, ListNode(
        2, ListNode(
            2, ListNode(
                1, None))))


head = ListNode(
    1, ListNode(
        2, ListNode(
                1, None)))

print(head.val)

arr = []
while head != None:
    arr.append(head.val)
    head = head.next

print(arr)
print(arr[::-1])
