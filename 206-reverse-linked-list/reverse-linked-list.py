# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr, nextn = None, head, None
        while curr:
            nextn = curr.next
            curr.next = prev
            prev = curr
            curr = nextn
        head = prev
        return prev
