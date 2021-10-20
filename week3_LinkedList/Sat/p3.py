class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


h1 = ListNode(
    1, ListNode(
        2, ListNode(
            3, ListNode(
                4, None))))

h2 = ListNode(
    5, ListNode(
        6, ListNode(
            7, ListNode(
                8, None))))
"""
arr = []
while h1 != None:
    arr.append(h1.val)
    h1 = h1.next
while h2 != None:
    arr.append(h2.val)
    h2 = h2.next

print(arr)

"""

h3 = ListNode(next =h1)
while h1 or h2:
    h2.next = h1.next
    h1.next = h2



arr2 = []
while h3.next != None:
    h3 = h3.next
    arr2.append(h3.val)

print(arr2)