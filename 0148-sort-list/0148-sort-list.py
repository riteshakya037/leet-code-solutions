# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # get size
        size = 0
        cur = head
        while cur is not None:
            cur = cur.next
            size += 1
        # split
        step = 1
        dummy = ListNode(None, head)
        while step < size:
            cur, pre = dummy.next, dummy
            while cur is not None:
                # split left half
                l = r = cur
                i = 1
                while i < step and r is not None:
                    r = r.next
                    i += 1
                if r is not None:
                    tmp = r.next
                    r.next = None
                    r = tmp

                # split right half
                cur = r
                i = 1
                while i < step and cur is not None:
                    cur = cur.next
                    i += 1
                if cur is not None:
                    tmp = cur.next
                    cur.next = None
                    cur = tmp

                # merge
                while l is not None and r is not None:
                    if l.val <= r.val:
                        pre.next, l = l, l.next
                    else:
                        pre.next, r = r, r.next
                    pre = pre.next
                pre.next = l if l is not None else r
                while (nxt := pre.next) is not None: pre = nxt
            step <<= 1
        return dummy.next