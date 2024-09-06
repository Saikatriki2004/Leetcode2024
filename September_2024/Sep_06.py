# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # Convert nums list to a set for faster lookups
        nums_set = set(nums)
        
        # Create a dummy node to handle edge cases (e.g., head node needs to be removed)
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize pointers
        prev = dummy
        current = head
        
        # Traverse the linked list
        while current:
            if current.val in nums_set:
                # Skip the current node
                prev.next = current.next
            else:
                # Move prev to the current node if it's not deleted
                prev = current
            # Move to the next node
            current = current.next
        
        # Return the modified list, starting from dummy.next (skipping dummy node)
        return dummy.next
if __name__ == "__main__":
    # Example linked list: 1 -> 2 -> 1 -> 2 -> 1 -> 2
    head = ListNode(1, ListNode(2, ListNode(1, ListNode(2, ListNode(1, ListNode(2))))))
    
    # Example nums list
    nums = [1]  # Remove all occurrences of 1
    
    # Create solution instance and call modifiedList
    sol = Solution()
    new_head = sol.modifiedList(nums, head)
    
    # Print the modified linked list
    current = new_head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next
