# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack=[[root,1]]
        res=0
        while stack:
            node,depth=stack.pop()
            print("node depth",node,depth)
            if node:
                res=max(res,depth)
                print("res",res)
                stack.append([node.left,depth+1])
                print("1",stack)
                stack.append([node.right,depth+1])
                print("2",stack)
        return res