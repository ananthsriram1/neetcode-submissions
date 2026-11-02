# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        p_queue = deque()
        q_queue = deque()

        p_queue.append(p)
        q_queue.append(q)

        while p_queue and q_queue:
            curr_p = p_queue.popleft()
            curr_q = q_queue.popleft()

            if curr_p == None and curr_q == None:
                continue
            elif curr_p and not curr_q:
                return False
            elif curr_q and not curr_p:
                return False
            if curr_p.val != curr_q.val:
                return False

                
            p_queue.append(curr_p.left)
            p_queue.append(curr_p.right)
            q_queue.append(curr_q.left)
            q_queue.append(curr_q.right)

        return True

        