class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for idx, char in enumerate(s):
            lastIndex[char] = idx

        partition = []
        size = end = 0

        for idx, char in enumerate(s):
            size = size + 1
            end = max(end, lastIndex[char])
            if idx == end:
                partition.append(size)
                size = 0
        return partition