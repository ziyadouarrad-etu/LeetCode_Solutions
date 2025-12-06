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

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or (not root.left and not root.right):
            return root

        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        self.invertTree(root.left)
        return self.isSameTree(root.left, root.right)
