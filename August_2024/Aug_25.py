from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(node):
            if not node:
                return []
            left = traverse(node.left)
            right = traverse(node.right)
            return left + right + [node.val]

        return traverse(root)
# Example to test the function
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

solution = Solution()
print(solution.postorderTraversal(root))  # Output: [3, 2, 1]
