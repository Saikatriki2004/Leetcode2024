# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head:
            return True  # Empty list is always a subpath
        if not root:
            return False  # Reached the end of the tree

        # Check if the current list node matches the current tree node
        def dfs(list_node, tree_node):
            if not list_node:
                return True  # End of linked list, subpath found
            if not tree_node:
                return False  # Reached end of tree without finding subpath
            if list_node.val != tree_node.val:
                return False  # Values do not match

            # Continue DFS on both left and right child
            return dfs(list_node.next, tree_node.left) or dfs(list_node.next, tree_node.right)

        # Start DFS at the current root or recursively check in left and right subtrees
        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
        # Example test
        if __name__ == "__main__":
       # Create linked list 4 -> 2 -> 8
       list_node = ListNode(4)
       list_node.next = ListNode(2)
       list_node.next.next = ListNode(8)

        # Create binary tree:
       #       1
       #      / \
       #     4   4
       #    /   / \
       #   2   2   6
       #  /   /
       # 8   1
       tree_root = TreeNode(1)
       tree_root.left = TreeNode(4)
       tree_root.right = TreeNode(4)
       tree_root.left.left = TreeNode(2)
       tree_root.left.left.left = TreeNode(8)
       tree_root.right.left = TreeNode(2)
       tree_root.right.left.left = TreeNode(1)
       tree_root.right.right = TreeNode(6)

       sol = Solution()
       print(sol.isSubPath(list_node, tree_root))  # Output: True
