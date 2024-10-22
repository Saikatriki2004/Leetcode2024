from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1  # Edge case if tree is empty
        
        # Queue for level-order traversal
        queue = deque([root])
        level_sums = []

        # Perform level-order traversal
        while queue:
            level_size = len(queue)
            level_sum = 0

            # Process all nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val

                # Add child nodes to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Store the sum of the current level
            level_sums.append(level_sum)

        # Sort the level sums in descending order
        level_sums.sort(reverse=True)

        # Check if we have at least 'k' levels
        if k > len(level_sums):
            return -1
        
        # Return the k-th largest level sum
        return level_sums[k - 1]
