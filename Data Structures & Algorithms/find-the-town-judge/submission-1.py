class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and not trust:
            # Only one person and no trust relations → that person is judge
            return 1

        score = [0] * (n + 1)  # ignore index 0

        for a, b in trust:
            score[a] -= 1  # a trusts someone → cannot be judge
            score[b] += 1  # b is trusted by a → more likely to be judge

        for person in range(1, n + 1):
            if score[person] == n - 1:
                return person

        return -1

# the judge:
# outgoing = 0
# incoming = n - 1 (everyone except themselves)

# Trick: Use one score array
# We can combine incoming and outgoing into a single number:
# Start with score[i] = 0 for all people.
# For a trust pair [a, b]:
# a trusts someone → bad for being judge → score[a] -= 1
# b is trusted by someone → good for being judge → score[b] += 1