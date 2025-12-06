# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (p and not q) or (not p and q):
            return False
        if p.val != q.val:
            return False
        if (p.left and not q.left) or (p.right and not q.right):
            return False
        if (q.left and not p.left) or (q.right and not p.right):
            return False
        bool1, bool2 = True, True
        if p.left:
            bool1 = self.isSameTree(p.left, q.left)
        if p.right:
            bool2 = self.isSameTree(p.right, q.right)
        return bool1 and bool2
