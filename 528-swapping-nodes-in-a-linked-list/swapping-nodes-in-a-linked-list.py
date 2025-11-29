# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p, q = head, head
        l = 0
        while p:
            l += 1
            p = p.next
        p = head
        for _ in range(k - 1):
            p = p.next
        for _ in range(l - k):
            q = q.next
        temp = p.val
        p.val = q.val
        q.val = temp
        return head
