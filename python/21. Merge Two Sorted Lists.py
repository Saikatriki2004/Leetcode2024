class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Create a dummy node to simplify the merging process
        dummy = ListNode()
        tail = dummy
        
        # Traverse both lists and merge them
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        # If there are remaining nodes in either list, append them
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        # Return the merged list, which starts from the next node of the dummy
        return dummy.next

# Example usage:
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Create lists for testing
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

# Merge lists
sol = Solution()
merged_list = sol.mergeTwoLists(list1, list2)
print_list(merged_list)  # Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None
