class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Connected but has a cycle → ❌ not a tree
        # No cycle but disconnected → ❌ not a tree
        # Connected + no cycle → ✅ tree

        # UNDIRECTED GRAPH - FIRST PROBLEM ON DIRECTED GRAPH
        if len(edges) > n-1:
            return False
        
        # help to reach to neighbours
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()

        def dfs(node, parent):
            if node in visit:
                return False
            
            visit.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        return dfs(0,-1) and len(visit) == n