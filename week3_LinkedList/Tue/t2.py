class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = ListNode(
        1, None)

'''
print(head.val)
print(head.next)'''

if head.next:
    print('there is')