class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Compute the length of the list
        length = 1
        old_tail = head
        
        while old_tail.next:
            old_tail = old_tail.next
            length += 1
        
        # Step 2: Normalize k
        k %= length
        if k == 0:
            return head
        
        # Step 3: Find the new tail and new head
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        old_tail.next = head
        new_tail.next = None
        
        return new_head
      # Example usage
if __name__ == "__main__":
    sol = Solution()
    head = list_to_linkedlist([1, 2, 3, 4, 5])
    rotated_head = sol.rotateRight(head, 2)
    print(linkedlist_to_list(rotated_head))  # Output: [4, 5, 1, 2, 3]
    
    head = list_to_linkedlist([0, 1, 2])
    rotated_head = sol.rotateRight(head, 4)
    print(linkedlist_to_list(rotated_head))  # Output: [2, 0, 1]
