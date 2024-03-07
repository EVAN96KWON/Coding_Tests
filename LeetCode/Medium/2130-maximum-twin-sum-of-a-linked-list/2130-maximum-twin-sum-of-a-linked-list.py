# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head

        # find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow

        # reverse second half
        reverse = None
        while middle:
            reverse, reverse.next, middle = middle, reverse, middle.next

        # now get pair sum
        ret = 0
        while head and reverse:
            ret = max(ret, head.val + reverse.val)
            head = head.next
            reverse = reverse.next

        return ret
