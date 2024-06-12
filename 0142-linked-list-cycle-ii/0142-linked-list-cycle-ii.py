# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow , fast  = head ,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: 
                temp1 = head
                temp2 = slow
                while temp1 != temp2:
                    temp1 = temp1.next
                    temp2 = temp2.next
                return temp1
        return None