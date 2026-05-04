class Solution:
    # DIRECTED GRAPH
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        edges = prerequisites
        # adjacency list representation
        adj_list = {c: [] for c in range(n)}
        for crs, pre in edges:
            adj_list[crs].append(pre)
        
        output = []  # output of topological sort
        visit = set()
        cycle = set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in adj_list[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        
        for c in range(n):
            if dfs(c) == False:
                return []
        return output