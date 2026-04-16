class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        # at most k stops -> k +1 flight (egdes)
        for i in range(k+1):

            # make a copy so this round only uses previous round values
            tmpPrices = prices.copy()

            # try relaxing every fling
            for s,d,p in flights:

                if prices[s] == float("inf"):
                    continue
                
                # if taking this flight gives cheaper cost, update
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p

            prices = tmpPrices

        return -1 if prices[dst] == float("inf") else prices[dst]
