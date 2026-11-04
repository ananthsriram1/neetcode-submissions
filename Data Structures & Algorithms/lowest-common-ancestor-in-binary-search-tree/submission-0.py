# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#for it to actually be a LCA, that means that one of the nodes has to be on the left and one of them has to be on the right, or its a parent of another. regardless we can add this into our logic
#brute force solution, you check all the children left and right, this looks like an n^2 solution though

#didnt realize it was a BST, so we just have to check the values. find a node where the greater one is to the right and the lesser is to the left


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        l = min(p.val, q.val)
        g = max(p.val, q.val)

        def helper(root):
            nonlocal l
            nonlocal g
            if root == None:
                return None
            print(root.val)
            if root.val > l and root.val > g:
                return helper(root.left)
            elif root.val < l and root.val < g:
                return helper(root.right)

            return root
        
        return helper(root)

