class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotoic increasing stack

        stack = []
        arr = temperatures
        n = len(arr)
        res = [0] * n 
        for i in range(n-1, -1 , -1): # monotonic stack like sliding window
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)

        return res
        