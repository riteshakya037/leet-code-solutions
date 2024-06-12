# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited_nodes = set()
        current_node = head
        
        while current_node:
            if current_node in visited_nodes:
                return current_node
            visited_nodes.add(current_node)
            current_node = current_node.next
        
        return None