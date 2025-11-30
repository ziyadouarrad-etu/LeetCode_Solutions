# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # single element edge case
        if not head or not head.next:
            return True
        # get to the middle and set head2
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        slow = slow.next
        head2 = slow

        # reverse the list starting from the middle
        prev = None
        curr = head2
        nextn = None
        while curr:
            nextn = curr.next
            curr.next = prev
            prev = curr
            curr = nextn
        head2 = prev

        # compare the 2 sublists
        p = head
        q = head2
        while q:
            print(p.val)
            print(q.val)
            if p.val != q.val:
                return False
            p = p.next
            q = q.next
        return True