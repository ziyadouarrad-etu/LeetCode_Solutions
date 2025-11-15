# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result=ListNode()
        r=result
        residue=0
        while True:
            sum=residue
            if l1:
                sum+=l1.val
                l1=l1.next
            if l2:
                sum+=l2.val
                l2=l2.next
            residue=sum//10
            r.val=sum%10
            if l1 or l2 or residue:
                r.next=ListNode()
                r=r.next
            else:
                break
        return result


        