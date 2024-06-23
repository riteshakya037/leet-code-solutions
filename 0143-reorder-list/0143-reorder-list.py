# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        queue = collections.deque()
        currentNode = head.next

        while currentNode:
            queue.append(currentNode)
            currentNode = currentNode.next
        
        currentNode = head
        while len(queue) > 1: 
            currentNode.next = queue.pop()
            currentNode = currentNode.next
            currentNode.next = queue.popleft()
            currentNode = currentNode.next
        
        if queue:
            currentNode.next = queue.pop()
            currentNode = currentNode.next
        
        currentNode.next = None
