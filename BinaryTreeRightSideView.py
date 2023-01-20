# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root: 
            return ans

        q = collections.deque()

        q.append(root)

        while(q):
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    print(f'after if \n node: {node.val}')
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                ans.append(rightSide.val)
        return ans
