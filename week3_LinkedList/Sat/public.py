
# Problem 1: Remove Duplicates from Sorted List
'''
Input: 1->1->2
Output: 1->2

Input: 1->1->2->3->3
Output: 1->2->3

'''

# UNDERSTAND
'''
(Test Cases)
Input: 1-> 1 -> 1
Output: 1

Input: null
Output: null

Input: 1
Output: 1
'''

# MATCH:
'''
Brute force: Using hashtable with pointers

2 pointer: p1 and p2
0.   1.   2.   3.   4
1 -> 2 -> 2
^		 			^
p1   			p2

p1 and p2 == 0.
p1.value==p2.next.value:
p2= p2.next

p1 ==0. and p2 ==1.
p1.value==p2.next.value:
p2= p2.next
....
p1 ==0. and p2==2.
p1.value==p2.next.value:
p1.next=p2.next

p1 and p2 ==3.
'''


# class LL_node:
#   def __init__(self, value):
#     self.value = value
#     sellf.next = None

# node1 = LL_node(2)

# node1.value

# def LL_q(head):
#   head.value
#   head.next


# Problem 2: Linked List Cycle

# UNDERSTAND
'''

(Test Case)
2->2->2 False
'''

# MATCH:
'''


'''
