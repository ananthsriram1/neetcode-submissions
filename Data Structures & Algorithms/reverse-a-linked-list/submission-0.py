# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        stack = []

        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next

        curr = dummy
        while stack:
            curr_node = stack.pop()
            curr.next = curr_node
            curr_node.next = None
            curr = curr.next

        return dummy.next