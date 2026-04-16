# my - we are not exploring all the possiblities.
# we are greedy for farthest occurance of that character

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        r = 0
        size = 0
        lastIndex = {}
        # mapping char and last occurance
        for idx, char in enumerate(s):
            lastIndex[char] = idx

        AnsPartition = []
        for idx, char in enumerate(s):
            size = size + 1
            r = max (r, lastIndex[char])
            if idx == r:
                AnsPartition.append(size)
                size = 0
        return AnsPartition

