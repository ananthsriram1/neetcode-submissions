# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        queue = deque()
        curr = head
        while curr:
            queue.append(curr)
            curr = curr.next
    

        flipped = False
        dummy = ListNode()
        curr = dummy

        while queue:
            
            if flipped:
                curr.next = queue.pop()
            else:
                curr.next = queue.popleft()
            
            curr = curr.next
            curr.next = None

            flipped = not flipped

        head = dummy.next