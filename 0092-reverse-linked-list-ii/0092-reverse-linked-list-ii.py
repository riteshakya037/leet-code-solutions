# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        prev, cur = None, head

        for _ in range(left - 1):
            prev, cur = cur, cur.next

        last_first_part = prev
        last_second_part = cur

        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = prev
            prev, cur = cur, nxt

        first_second_part = prev

        if last_first_part:
            last_first_part.next = first_second_part
        else:
            head = first_second_part

        last_second_part.next = cur

        return head
