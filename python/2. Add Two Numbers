# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Initialize dummy node and current pointer
        dummy = ListNode(0)
        current = dummy
        carry = 0

        # Traverse both lists
        while l1 or l2 or carry:
            # Get values from current nodes or 0 if one list is shorter
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate new sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            new_val = total % 10
            
            # Create new node with the new value
            current.next = ListNode(new_val)
            current = current.next

            # Move to the next nodes
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next
