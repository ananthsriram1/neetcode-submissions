# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        #init final list
        dummy = ListNode()
        curr = dummy

        #init pointers so we can successfully iterate through both of the lists
        l1_curr = l1
        l2_curr = l2

        #init carry
        carry = 0

        #iteration through the list
        while l1_curr and l2_curr:

            current_sum = l1_curr.val + l2_curr.val + carry

            #check if theres any carry over
            if current_sum >= 10:
                carry = 1
                current_sum -= 10
            else:
                carry = 0

            #add the the final list
            new = ListNode(current_sum)
            curr.next = new
            curr = curr.next

            #move pointers forward
            l1_curr = l1_curr.next
            l2_curr = l2_curr.next

        while l1_curr:
            current_sum = l1_curr.val + carry

            #check if theres any carry over
            if current_sum >= 10:
                carry = 1
                current_sum -= 10
            else:
                carry = 0

            #add the the final list
            new = ListNode(current_sum)
            curr.next = new
            curr = curr.next

            #move pointers forward
            l1_curr = l1_curr.next

        while l2_curr:
            current_sum = l2_curr.val + carry

            #check if theres any carry over
            if current_sum >= 10:
                carry = 1
                current_sum -= 10
            else:
                carry = 0

            #add the the final list
            new = ListNode(current_sum)
            curr.next = new
            curr = curr.next

            #move pointers forward
            l2_curr = l2_curr.next

        if carry != 0:
            new = ListNode(carry)
            curr.next = new

        return dummy.next
        
        