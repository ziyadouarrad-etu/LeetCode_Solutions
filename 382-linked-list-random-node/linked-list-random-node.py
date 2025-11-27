# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.len = 0
        
        current = head
        while current:
            self.len += 1
            current = current.next


    def getRandom(self) -> int:
        current=self.head
        for i in range(random.randint(0,self.len-1)):
            current=current.next
        return current.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()