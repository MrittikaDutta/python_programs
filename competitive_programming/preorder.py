def preorder(root):
   
    # code here
    if root is None:
        return []
    
    # Recursive case: perform preorder traversal
    result = []
    result.append(root.data)  # Visit the current node
    result.extend(preorder(root.left))  # Traverse the left subtree
    result.extend(preorder(root.right))  # Traverse the right subtree
    
    return result