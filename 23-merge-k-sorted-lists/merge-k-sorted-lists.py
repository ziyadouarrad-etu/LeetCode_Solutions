# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        newList = ListNode()
        temp = newList

        while True:
            idx_min = -1
            val_min = float("inf")

            for idx, node in enumerate(lists):
                if node and node.val < val_min:
                    idx_min = idx
                    val_min = node.val

            if idx_min == -1:
                break
                
            temp.next = ListNode(val_min)
            temp = temp.next
            
            lists[idx_min] = lists[idx_min].next

        return newList.next




        