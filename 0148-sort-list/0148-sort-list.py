# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
  
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy.next

        lst = []
        while curr:
            lst.append(curr.val)
            curr = curr.next

        lst.sort()

        curr = dummy.next
        for v in lst:
            curr.val = v
            curr = curr.next

        return dummy.next