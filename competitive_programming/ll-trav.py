class Solution:
    def display(self,node):
        if node is None:
            return []
        
        result = []
        print(node.data,end=' ')
        result.append(node.data)  # Append current node's data to the result list
        
        if node.next is not None:
            result.extend(self.display(node.next))  # Recursively display nodes in the rest of the linked list
        
        return result