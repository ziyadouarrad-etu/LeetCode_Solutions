# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root: Optional[TreeNode], k):
        if not root or not k:
            return
        self.helper(root.left, k)
        if self.k:
            self.a = root.val
            self.k -= 1
            self.helper(root.right, k)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.helper(root, k)
        return self.a
