from math import gcd

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        curr = head
        
        while curr and curr.next:
            # Find GCD between current node and next node
            gcd_value = gcd(curr.val, curr.next.val)
            
            # Create a new node with the GCD value
            new_node = ListNode(gcd_value)
            
            # Insert the new node between curr and curr.next
            new_node.next = curr.next
            curr.next = new_node
            
            # Move to the next pair (skip the newly inserted GCD node)
            curr = new_node.next
            
        return head

# Example usage:
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Example linked list: 18 -> 24 -> 9
head = ListNode(18, ListNode(24, ListNode(9)))
solution = Solution()
new_head = solution.insertGreatestCommonDivisors(head)
print_list(new_head)  # Output will show inserted GCD values
