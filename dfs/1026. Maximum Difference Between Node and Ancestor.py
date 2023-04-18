from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.max = 0
        self.dfs(root, [])
        return self.max
    
    def dfs(self, node, path):
        if not node:
            self.max = max(self.max, max(path)-min(path))
            return
        
        path.append(node.val)
        self.dfs(node.left, path)
        self.dfs(node.right, path)
        path.pop()