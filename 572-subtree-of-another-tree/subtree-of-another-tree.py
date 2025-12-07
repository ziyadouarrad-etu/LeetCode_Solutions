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

        bool1 = self.isSameTree(p.left, q.left)
        bool2 = self.isSameTree(p.right, q.right)
        return bool1 and bool2

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isSameTree(root, subRoot):
            return True
        bool1, bool2 = False, False
        if root.left:
            bool1 = self.isSubtree(root.left, subRoot)
        if root.right:
            bool2 = self.isSubtree(root.right, subRoot)
        return bool1 or bool2
