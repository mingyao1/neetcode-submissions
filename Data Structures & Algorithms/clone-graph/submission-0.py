"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mp = {}

        def clone(node):
            if node in mp:
                return mp[node]
            
            copy = Node(node.val)
            mp[node] = copy
            #print(mp)
            for n in node.neighbors:
                copy.neighbors.append(clone(n))

            return copy
        
        if node: 
            return clone(node) 
        else: 
            return None