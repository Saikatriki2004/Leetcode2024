# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        count = itertools.count()  # Unique sequence count
        
        # Initialize the heap with the head of each list as (value, count, node)
        for i in range(len(lists)):
            if lists[i] is not None:
                heappush(min_heap, (lists[i].val, next(count), lists[i]))
        
        dummy = ListNode()
        current = dummy
        
        # Extract the smallest element and push its next node to the heap
        while min_heap:
            _, _, smallest_node = heappop(min_heap)
            current.next = smallest_node
            current = current.next
            if smallest_node.next:
                heappush(min_heap, (smallest_node.next.val, next(count), smallest_node.next))
        
        return dummy.next

# Helper function to create linked lists from a list of lists
def create_linked_lists(list_of_values):
    lists = []
    for values in list_of_values:
        if not values:
            lists.append(None)
            continue
        head = ListNode(values[0])
        current = head
        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next
        lists.append(head)
    return lists

# Helper function to print linked list
def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Example usage:
list_of_values = [[1,4,5],[1,3,4],[2,6]]
lists = create_linked_lists(list_of_values)
sol = Solution()
merged_list = sol.mergeKLists(lists)
print_linked_list(merged_list)  # Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6 -> None
