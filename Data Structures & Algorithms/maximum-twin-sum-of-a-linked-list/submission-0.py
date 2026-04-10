# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []
        max_sum = 0
        fast = slow = head 
        while fast:
            stack.append(slow.val)
            fast = fast.next.next
            slow = slow.next
        while slow:
            max_sum = max(max_sum, stack.pop() + slow.val)
            slow = slow.next
        return max_sum
        