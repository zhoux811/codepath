class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Problem 1: Add Two Numbers
'''
Input: 2 -> 4 -> 3,  5 -> 6 -> 4
Output: 7 -> 0 -> 8

Explanation: 342 + 465 = 807
'''

# UNDERSTAND:
'''
(Test Case)
Input: 1 -> 2 -> 3,  4 -> 5 -> 6
Output: 975

Input: 5 -> 5, 5 -> 4
Output: 0 -> 0 -> 1

(Questions)
- 4, 3, and its output would be 7? 
	- would this be a linked list?
'''

# MATCH/PLAN:
'''
- check if the linkedlists are equal
	- create a clone LL1 (greatest length LinkedList is cloned first)
- iterate through the LL1 and LL2
	- at each iteration check the lengths
	- sum the two corresponding nodes of the lengths and clone 	the nodes
		- if they're not corresponding nodes, then take the 	remainders from prev sum and add it to the longest length linkedlist
'''


# IMPLENTATION:
# def check_len(_LL = ListNode):
#   length = 0
#   while _LL:
#     length+=1
#     _LL = _LL.next
#   return length

# def compare_length_then_return_longer_one(_LL1, _LL2):
#   if check_len(_LL1) >=  check_len(_LL2):
#     return _LL1
#   else:
#     return _LL2

# def add_two_n(LL1, LL2):
#   new_LL = ListNode(val=0, next = None)

#   while LL1 or LL2:
#     pass

def addTwoNumbers(l1: ListNode, l2: ListNode):
    # initialize dummy head
    dummyHead = ListNode(0)

    # p and q are clones of the LinkedLists
    p = l1
    q = l2

    # dummy node of dummy node
    curr = dummyHead

    # initialize carry to use later
    carry = 0;

    # clone nodes are not empty do the following...
    while p is not None or q is not None:

        # get the value of the nodes and assign variable
        # if None then == 0
        x = p.val if p is not None else 0
        y = q.val if q is not None else 0

        # find sum with carry
        sum = carry + x + y

        # carry is floor divide
        carry = sum // 10

        # placeholder is modulo
        curr.next = ListNode(sum % 10)

        # iterate to next node
        curr = curr.next

        # only iterate to next node if current value exists
        if p is not None:
            p = p.next
        if q is not None:
            q = q.next

    # If carry > 0 (also could be greater than the length of Inpus LinkedLists)
    # create a new node to the linked list
    if carry > 0:
        curr.next = ListNode(carry)

    # return the starting value of dummy.next since dummy is a placeholder to initially start
    return dummyHead.next


# 2 -> 4 -> 3,  5 -> 6 -> 4
# l1 = ListNode(
#   2, ListNode(
#     4, ListNode(
#       3, None)))

# l2 = ListNode(
#   5, ListNode(
#     6, ListNode(
#       4, None)))


# 5 -> 0,  5 -> 0
l1 = ListNode(
    0, ListNode(
        5, None))

l2 = ListNode(
    0, ListNode(
        5, None))

dummynext = (addTwoNumbers(l1, l2))

while dummynext:
    print(dummynext.val)
    dummynext = dummynext.next
