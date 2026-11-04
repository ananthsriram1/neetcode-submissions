# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def helper(r, sr):
            if not r and not sr:
                return True
            elif (not r and sr) or (r and not sr):
                return False

            if r.val == sr.val:
                return True and helper(r.left, sr.left) and helper(r.right, sr.right)

            return False
        
        queue = deque()
        queue.append(root)

        while queue:
            curr = queue.popleft()

            if curr.val == subRoot.val and helper(curr, subRoot):
                return True

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        return False
        