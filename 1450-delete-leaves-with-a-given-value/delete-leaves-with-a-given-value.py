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
            if not root:
                return None

            # special case: root is a removable leaf
            if not root.left and not root.right and root.val == target:
                return None

            stack = [root]
            changed = False
            while stack:
                node = stack.pop()

                if node.left:
                    if (
                        not node.left.left and not node.left.right
                    ) and node.left.val == target:
                        node.left = None
                        changed = True
                    else:
                        stack.append(node.left)

                if node.right:
                    if (
                        not node.right.left and not node.right.right
                    ) and node.right.val == target:
                        node.right = None
                        changed = True
                    else:
                        stack.append(node.right)

        return root
