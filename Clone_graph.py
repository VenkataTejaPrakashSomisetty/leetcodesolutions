class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return None
        
        clone_map = {} 
        
        def dfs(curr_node):
            if curr_node in clone_map:
                return clone_map[curr_node]  
            
            
            cloned_node = Node(curr_node.val)
            clone_map[curr_node] = cloned_node  
            
    
            for neighbor in curr_node.neighbors:
                cloned_node.neighbors.append(dfs(neighbor))
            
            return cloned_node
        
        return dfs(node)
