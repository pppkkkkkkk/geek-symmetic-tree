'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def isSymmetric(self, root):
        
        def dfs(left, right):
            
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.data != right.data:
                return False
                
            return dfs(left.left, right.right) and dfs(left.right, right.left)
            
        return dfs(root.left, root.right)
        