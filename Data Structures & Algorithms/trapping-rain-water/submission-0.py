class Solution:
    def trap(self, height: List[int]) -> int:
        # boundary pr decision lena hai
        
        arr = height
        n = len(arr)
        if n == 0:
            return 0
        l = 0
        r = n - 1
        leftMax = arr[l] # iss pr paani nhi rukega
        rightMax = arr[r] # iss pr pani nhi rukega
        res = 0
        while l < r:
            if leftMax < rightMax:
                # left max chota hai toh -> left mein movement
                l += 1
                leftMax = max(leftMax, arr[l])
                res += leftMax - arr[l]
            else:
                # rightmax chota hai toh -> right mein movement
                r -= 1
                rightMax = max(rightMax, arr[r])
                res += rightMax - arr[r]

        return res



