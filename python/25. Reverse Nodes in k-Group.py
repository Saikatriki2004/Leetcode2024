class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Function to reverse a part of the linked list
        def reverseLinkedList(head, k):
            new_head = None
            ptr = head
            while k:
                next_node = ptr.next
                ptr.next = new_head
                new_head = ptr
                ptr = next_node
                k -= 1
            return new_head
        
        # Count the number of nodes in the linked list
        count = 0
        ptr = head
        while ptr:
            ptr = ptr.next
            count += 1
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while count >= k:
            curr = prev.next
            next_group = curr
            for _ in range(k):
                next_group = next_group.next
            
            new_head = reverseLinkedList(curr, k)
            prev.next = new_head
            curr.next = next_group
            prev = curr
            count -= k
        
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
values = [1, 2, 3, 4, 5]
k = 2
head = create_linked_list(values)
sol = Solution()
reversed_head = sol.reverseKGroup(head, k)
print_linked_list(reversed_head)  # Output: 2 -> 1 -> 4 -> 3 -> 5 -> None

values = [1, 2, 3, 4, 5]
k = 3
head = create_linked_list(values)
reversed_head = sol.reverseKGroup(head, k)
print_linked_list(reversed_head)  # Output: 3 -> 2 -> 1 -> 4 -> 5 -> None
