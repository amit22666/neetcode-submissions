from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        def canFinish(capacity: int) -> bool:
            days_needed = 1
            current_load = 0

            for w in weights:
                if current_load + w > capacity:
                    days_needed += 1
                    current_load = w
                    if days_needed > days:
                        return False
                else:
                    current_load += w

            return True

        while l < r:
            mid = (l + r) // 2
            if canFinish(mid):
                r = mid
            else:
                l = mid + 1

        return l