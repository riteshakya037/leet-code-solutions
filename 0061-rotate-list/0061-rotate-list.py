# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        length = 1
        last_ele = head
        while last_ele.next is not None:
            last_ele = last_ele.next
            length += 1
        last_ele.next = head

        k = k % length

        curr = head
        for x in range(length - k - 1):
            curr = curr.next

        answer = curr.next
        curr.next = None
        return answer
