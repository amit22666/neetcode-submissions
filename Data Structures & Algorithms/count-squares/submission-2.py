
class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: [int, int]) -> None:
        x, y = point
        self.points[(x, y)] += 1

    def count(self, point: [int, int]) -> int:
        x, y = point
        total = 0

        # Copy of items banalo taaki iteration safe ho
        items = list(self.points.items())

        for (px, py), freq in items:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue

            # Square ke liye required points check karo
            total += freq * self.points[(px, y)] * self.points[(x, py)]

        return total
