# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # head alone edge case
        if not head or not head.next:
            return None

        # get the size of the linked list
        l = 0
        p = head
        while p:
            l += 1
            p = p.next

        # l == n edge case
        if l==n:
            return head.next
        
        # remove the nth node from the end
        p = head
        q = p
        for _ in range(l - n):
            q = p
            p = p.next
        q.next = p.next

        return head
