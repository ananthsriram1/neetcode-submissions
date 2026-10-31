# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1_curr = list1
        list2_curr = list2
        
        dummy = ListNode()
        curr = dummy

        while list1_curr and list2_curr:
            choice = None
            if list1_curr.val < list2_curr.val:
                choice = list1_curr
                list1_curr = list1_curr.next
            else:
                choice = list2_curr
                list2_curr = list2_curr.next
            
            curr.next = choice
            choice.next = None
            curr = curr.next

        
        remaining = None
        if list1_curr:
            remaining = list1_curr
        elif list2_curr:
            remaining = list2_curr

        while remaining:
            curr.next = remaining
            remaining = remaining.next
            curr = curr.next
            curr.next = None

        return dummy.next
