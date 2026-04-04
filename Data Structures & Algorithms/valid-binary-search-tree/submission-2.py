# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        inf = math.inf
        def check(node, lb, ub):
            if not node:
                return True
            if node.val <= lb or node.val >= ub:
                return False
            return check(node.left, lb, node.val) and check(node.right, node.val, ub)

        return check(root, -inf, inf)

