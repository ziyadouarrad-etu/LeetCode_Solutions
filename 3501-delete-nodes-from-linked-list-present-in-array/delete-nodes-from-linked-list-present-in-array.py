# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums=set(nums)
        while head.val in nums:
            head = head.next

        p = head
        while p.next:
            if p.next.val in nums:
                p.next = p.next.next
            else:
                p = p.next

        return head
