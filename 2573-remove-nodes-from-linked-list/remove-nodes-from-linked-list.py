# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head
        nextn=None
        while (curr):
            nextn=curr.next
            curr.next=prev
            prev=curr
            curr=nextn
        head=prev

        newHead=None
        p=head
        max_=float('-inf')
        while (p):
            if p.val>=max_:
                temp=ListNode(p.val)
                temp.next=newHead
                newHead=temp
                max_=p.val
            p=p.next
        return newHead



        