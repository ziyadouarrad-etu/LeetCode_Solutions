# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:
    
        changed = True
        while changed:
            stack = [root]
            changed = False
            while stack:
                node = stack.pop()
                if (
                    node.left
                    and (not node.left.left and not node.left.right)
                    and node.left.val == target
                ):
                    node.left = None
                    changed = True
                if (
                    node.right
                    and (not node.right.left and not node.right.right)
                    and node.right.val == target
                ):
                    node.right = None
                    changed = True
                if node.left and node.right:
                    stack.extend([node.left, node.right])
                elif node.left:
                    stack.append(node.left)
                elif node.right:
                    stack.append(node.right)

        if not root or (not root.left and not root.right and root.val == target):
            return None
        return root
