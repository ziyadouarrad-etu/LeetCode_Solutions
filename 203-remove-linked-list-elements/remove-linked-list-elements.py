# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        newHead = None
        curr = newHead
        p = head
        while p:
            if p.val == val:
                p = p.next
                continue
            temp = ListNode(p.val)
            if newHead == None:
                newHead = temp
            else:
                curr.next = temp
            curr = temp
            p = p.next
        return newHead
