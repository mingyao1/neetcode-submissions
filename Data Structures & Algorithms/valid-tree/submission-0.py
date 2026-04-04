class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i: [] for i in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()

        def dfs(node, pre):
            if node in visited:
                return False
            
            visited.add(node)

            for n in graph[node]:
                if n == pre: continue

                if not dfs(n, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n
            

            
            