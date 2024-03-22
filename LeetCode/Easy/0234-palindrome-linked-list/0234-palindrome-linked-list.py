# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        if len(vals) <= 1:
            return True
        if len(vals) % 2 == 1:
            vals.pop(len(vals) // 2)
        left, right = vals[: len(vals) // 2], vals[len(vals) // 2 :][::-1]
        if left == right:
            return True
        return False
