class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search on col to find correct row
        # top  = 0 and bot = rows -1
        l = 0
        r = len(matrix) - 1 # rows

        rows = len(matrix)
        cols = len(matrix[0])

        # if matrix[0][0] > target or  matrix[row-1][col-1] < target:
        #     return False

        
        row = -1
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[mid][-1]:  # compare with last value of row
                l = mid + 1
            elif target < matrix[mid][0]: # compare with first value of that row
                r = mid - 1
            else:
                row = mid
                break  # value lies with in this range

        if row == -1:
            return False

        l, r = 0, cols - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                return True
        
        return False
        
       

        #FIRST PORTION OF BINARY SEARCH TO FIND THE CORRECT ROW
        # while top less than of equal ot bottom
            # calcuate mid with top and bottom
            # compare target and matrix of mid, -1. Target if big then mid
                # movement bottom / down 
            # elif compare target and matrix of mid, -1
                # movement top / up
            # else:
                # break

        # check corner case non of the row contain the target value

        

        # FIND CORRECT ELEMENT IN THAT ROW
        # calcuate get row from mid calculation
        # while l <= r
            # calculate mid
            # compare target and row,middle
                # move right
            # elif compare target and row, middle
                # move left
            # else
                # return true
        # return False


