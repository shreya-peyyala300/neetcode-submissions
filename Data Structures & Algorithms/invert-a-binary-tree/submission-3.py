# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue=deque([root])
        while queue:
            data=queue.popleft()
            data.left,data.right=data.right,data.left
            if data.left:
                queue.append(data.left)
            if data.right:
                queue.append(data.right)
        return root