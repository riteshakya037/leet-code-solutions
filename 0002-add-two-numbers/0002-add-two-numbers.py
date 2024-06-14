# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        def linked_list_to_num(node):
            num = 0
            count = 1
            while node:
                num += node.val * count
                count = count * 10
                node = node.next
            return num

        def num_to_linked_list(num):
            finalh = ListNode(-1)
            helper = finalh

            while num != 0:
                helper.next = ListNode(num % 10)
                num = num // 10
                helper = helper.next
            return finalh

        num1 = linked_list_to_num(l1)
        num2 = linked_list_to_num(l2)

        result = num1 + num2
        if result == 0:
            return ListNode(0)

        finalh = num_to_linked_list(result)

        return finalh.next
