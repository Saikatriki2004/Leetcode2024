# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Base case: both nodes are None
        if not root1 and not root2:
            return True
        # If one of the nodes is None or their values are different
        if not root1 or not root2 or root1.val != root2.val:
            return False
        
        # Recursively check the two possible ways of matching:
        # 1. Without flipping
        # 2. With flipping left and right children
        return (
            (self.flipEquiv(root1.left, root2.left) and 
             self.flipEquiv(root1.right, root2.right))
            or
            (self.flipEquiv(root1.left, root2.right) and 
             self.flipEquiv(root1.right, root2.left))
        )
