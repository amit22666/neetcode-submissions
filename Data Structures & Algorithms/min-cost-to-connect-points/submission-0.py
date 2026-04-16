class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # points = [[0,0],[2,2],[3,3],[2,4],[4,2]]
        N = len(points)
        adj = { i: [] for i in range(N)}
        
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1,N): 
                # x1,y1 ka baki saare points ke saath dist
                x2, y2 = points[j]
                dist = abs(x2-x1) + abs(y2-y1)
                adj[i].append((dist,j)) # in adj we are storing index
                adj[j].append((dist,i)) # un-directional graph

        # prim
        res = 0
        visit = set()
        minH = [[0,0]] # cost , point

        while len(visit) < N:
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            res = res + cost
            visit.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])
        return res

