class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # solution exist
        if sum(gas) < sum(cost):
            return -1
        res = 0
        total = 0
        for i in range(len(gas)):
            # imp = we are not increasing res in a iteration
            # instead we are checking if the current index can be answer or not
            total = total + gas[i] - cost[i]
            print(f"total = {total}")
            print(f"res = {res}")
            if total < 0:
                total = 0
                res = i+1
                print(f"result inside = {res}")
        print(f"final res = {res}")
        return res
        