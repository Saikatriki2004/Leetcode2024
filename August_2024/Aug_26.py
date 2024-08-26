from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        
        result = []
        
        # Recursive function to perform postorder traversal
        def traverse(node):
            for child in node.children:
                traverse(child)
            result.append(node.val)
        
        traverse(root)
        return result
# Constructing the N-ary tree
#         1
#       / | \
#      3  2  4
#     / \
#    5   6

node5 = Node(5)
node6 = Node(6)
node3 = Node(3, [node5, node6])
node2 = Node(2)
node4 = Node(4)
root = Node(1, [node3, node2, node4])

solution = Solution()
result = solution.postorder(root)
print(result)  # Output: [5, 6, 3, 2, 4, 1]
