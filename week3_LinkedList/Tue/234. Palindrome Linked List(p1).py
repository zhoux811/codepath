# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []

        arr.append(head.val)
        while head.next:
            arr.append(head.next.val)
            head = head.next
        print(arr)
        return True if arr == arr[::-1] else False