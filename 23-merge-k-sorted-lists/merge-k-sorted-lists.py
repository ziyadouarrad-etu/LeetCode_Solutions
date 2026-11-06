# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return None

        newList = ListNode()
        temp = newList
        nb_lists = len(lists)
        we_good = False

        for L in lists:
            if L != None:
                we_good = True
                break

        while we_good:

            idx_min = 0
            val_min = float("inf")
            for idx, node in enumerate(lists):
                if node and node.val < val_min:
                    idx_min = idx
                    val_min = node.val

            print(val_min)
            temp.next = ListNode()
            temp = temp.next
            temp.val = val_min
            
            lists[idx_min] = lists[idx_min].next

            we_good = False
            for L in lists:
                if L != None:
                    we_good = True
                    break

        return newList.next




        