class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Number of nodes
        n = len(edges)
        
        # Parent array: initially each node is its own parent
        parent = [i for i in range(n + 1)]

        # Find function with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # path compression
            return parent[x]

        # Union function
        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            # If both nodes have same root, cycle detected
            if rootX == rootY:
                return False
            
            # Otherwise, connect them
            parent[rootY] = rootX
            return True

        # Process edges one by one
        for u, v in edges:
            if not union(u, v):
                return [u, v]
