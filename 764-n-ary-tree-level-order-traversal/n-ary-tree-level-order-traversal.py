"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
        # Empty tree edge case
        if not root:
            return []

        # Initialize lists that will be used as well as the result list
        curr = [root]
        result = [[root.val]]

        # Loop through all nodes in the current level getting there values and there children
        while curr:
            temp = []
            next_level = []
            for node in curr:
                for child in node.children:
                    next_level.append(child)
                    temp.append(child.val)
            if temp:
                result.append(temp)
            curr = next_level
        return result
