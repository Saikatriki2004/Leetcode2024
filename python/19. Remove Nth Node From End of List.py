class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        
        # Move first pointer n steps ahead
        for _ in range(n + 1):
            first = first.next
        
        # Move both pointers until first reaches the end
        while first:
            first = first.next
            second = second.next
        
        # Remove the nth node from the end
        second.next = second.next.next
        
        return dummy.next

# Example usage:
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Create linked list [1,2,3,4,5]
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

sol = Solution()
n = 2
new_head = sol.removeNthFromEnd(head, n)
printList(new_head)  # Output: 1 -> 2 -> 3 -> 5 -> None
