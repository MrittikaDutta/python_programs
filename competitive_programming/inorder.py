class Solution:
    def InOrder(self,root):
        if root is None:
            return []
        
        result = []
        result.extend(self.InOrder(root.left)) 
        result.append(root.data)
        result.extend(self.InOrder(root.right))
        
        return result
