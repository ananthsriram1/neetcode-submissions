# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next

        target = size - n
        if target == 0:
            return head.next

        pointer = None
        curr = head
        for i in range(0, target):
            if i == target - 1:
                pointer = curr

            curr = curr.next

        pointer.next = pointer.next.next
        return head