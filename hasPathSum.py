# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # subsets = []
        ans = False
        
        def backtracking(root, prev):
            if not root:
                return False
        
            # subset.append(root.val)
            prev += root.val
            if(prev == targetSum):
                if(root.left == None and root.right == None):
                    ans=True
                    return ans
            left = backtracking(root.left, prev)
            right = backtracking(root.right, prev)
            prev -= root.val
            if left or right:
                return True
            return False
        return backtracking(root, 0)
