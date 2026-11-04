# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        rv = []

        queue = deque()
        queue.append(root)

        while queue:
            curr_list = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                curr_list.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            rv.append(curr_list)

        return rv

        