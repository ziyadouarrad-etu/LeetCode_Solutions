# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root: Optional[TreeNode]):
        if not root.left:
            return
        left, right = True, True
        if root.left.val > root.val:
            left = False
            self.min2 = (
                root.left.val if self.min2 == -1 else min(self.min2, root.left.val)
            )
        if root.right.val > root.val:
            right = False
            self.min2 = (
                root.right.val if self.min2 == -1 else min(self.min2, root.right.val)
            )
        if left:
            self.helper(root.left)
        if right:
            self.helper(root.right)

    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.min = root.val
        self.min2 = -1
        self.helper(root)
        return self.min2
