# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result=ListNode()
        r=result
        while (list1 and list2):
            r.next=ListNode()
            r=r.next
            if list1.val<list2.val:
                r.val=list1.val
                list1=list1.next
            else:
                r.val=list2.val
                list2=list2.next

        while list1:
            r.next=ListNode(val=list1.val)
            list1=list1.next
            r=r.next
        
        while list2:
            r.next=ListNode(val=list2.val)
            list2=list2.next
            r=r.next
        
        return result.next