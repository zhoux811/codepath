class DLNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


n1 = DLNode(1)
n2 = DLNode(2)
n3 = DLNode(3)
n4 = DLNode(4)
n5 = DLNode(5)
n6 = DLNode(6)
n7 = DLNode(7)

n1.next = n2
n1.prev =None

n2.next = n3
n2.prev = n1

n3.next = n4
n3.prev = n2

n4.next = n5
n4.prev = n3

n5.next = n6
n5.prev = n4

n6.next = n7
n6.prev = n5

n7.next = None
n7.prev =