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
            # Why? len(queue) > 1 : To avoid the empty queue.pops()
            currentNode.next = queue.pop() # last node in the deque
            currentNode = currentNode.next
            currentNode.next = queue.popleft() # first node in the deque
            currentNode = currentNode.next
        
        # Why?: if len(queue) is odd we will have a 1 node to add
        if queue:
            currentNode.next = queue.pop()
            currentNode = currentNode.next
        
        # Why?: To avoid the cycle
        currentNode.next = None