# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        before_slow = slow = fast = head
        while fast.next:
            before_slow, slow = slow, slow.next
            fast = fast.next
            if fast.next:
                fast = fast.next
                if not fast.next:  # Move middle entry to left half in odd case
                    before_slow, slow = slow, slow.next
        before_slow.next = None

        # Reverse second half
        next_node, slow.next = slow.next, None
        while next_node:
            next_node.next, slow, next_node = slow, next_node, next_node.next
        
        # Interleave
        while head and fast:
            head.next, head = fast, head.next
            fast.next, fast = head, fast.next
