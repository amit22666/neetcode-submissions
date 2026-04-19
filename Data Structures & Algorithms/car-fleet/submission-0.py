from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair position and speed, sort by position descending
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        curFleetTime = 0.0

        for pos, sp in cars:
            time = (target - pos) / sp

            # If this car cannot catch the fleet ahead, it forms a new fleet
            if time > curFleetTime:
                fleets += 1
                curFleetTime = time

        return fleets