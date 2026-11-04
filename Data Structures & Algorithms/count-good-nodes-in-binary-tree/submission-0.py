# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_count = 0

        def helper(root, current_max):
            nonlocal good_count

            if root.val >= current_max:
                good_count += 1

            current_max = max(root.val, current_max)
            if root.left:
                helper(root.left, current_max)
            if root.right:
                helper(root.right, current_max)

        helper(root, root.val)
        return good_count
        