class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix product and suffix product

        arr = nums
        n = len(arr)
        answer = [1] * n
        # prefix product
        for i in range(1, n):
            answer[i] = arr[i-1] * answer[i-1]

        # suffix product
        suffix = 1
        for i in range(n-1,-1, -1):
            answer[i] *= suffix
            suffix *= arr[i]

        return answer
