class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Iterate through the list while there are at least two more nodes to process
        while prev.next and prev.next.next:
            first = prev.next
            second = first.next
            
            # Swap the nodes
            first.next = second.next
            second.next = first
            prev.next = second
            
            # Move the prev pointer two nodes ahead
            prev = first
        
        return dummy.next

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to print linked list
def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Example usage:
values = [1, 2, 3, 4]
head = create_linked_list(values)
sol = Solution()
swapped_head = sol.swapPairs(head)
print_linked_list(swapped_head)  # Output: 2 -> 1 -> 4 -> 3 -> None
