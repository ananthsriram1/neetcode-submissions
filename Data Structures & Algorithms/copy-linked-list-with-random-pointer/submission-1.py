"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        copy_map = {}
        
        curr = head
        dummy = Node(0)
        copy_curr = dummy

        while curr:
            new = Node(curr.val)
            copy_map[curr] = new

            copy_curr.next = new
            copy_curr = copy_curr.next
            curr = curr.next    

        curr = head

        while curr:
            if curr.random:
                copy_map[curr].random = copy_map[curr.random]
            else:
                copy_map[curr].random = None
            curr = curr.next

        return dummy.next

        