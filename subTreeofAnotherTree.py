# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return False

        if self.sameTree(root, subRoot):
            print(3)
            return True
        print(0)
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, root, root2):
        if not root and not root2:
            print(1)
            return True

        if root and root2 and root.val == root2.val:
            print(2)
            return self.sameTree(root.left, root2.left) and self.sameTree(root.right, root2.right)
        return False