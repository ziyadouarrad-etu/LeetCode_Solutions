"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


class Solution:
    def helper(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return self.result
        self.result.append(root.val)
        for child in root.children:
            self.helper(child)
        return self.result

    def preorder(self, root: "Node") -> List[int]:
        self.result = []
        return self.helper(root)
