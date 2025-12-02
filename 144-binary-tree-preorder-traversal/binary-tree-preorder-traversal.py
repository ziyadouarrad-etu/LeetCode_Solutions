# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = []

    def helper(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return self.result
        self.result.append(root.val)
        self.helper(root.left)
        self.helper(root.right)
        return self.result

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        return self.helper(root)