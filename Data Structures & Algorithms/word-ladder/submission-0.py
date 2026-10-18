class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # graph ka problem hai
        # adjencency list pr bfs krna
        # regex : list of words which match that regex

        if endWord not in wordList:
            return 0

        nei = collections.defaultdict(list)
        wordList.append(beginWord)

        # create adjencency list
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)
        # adjencencylist creation done

        # bfs
        q = deque([beginWord])
        visit = set([beginWord])
        res = 1

        while q: # level
            for i in range(len(q)): # if a level has more than 1 element
                word = q.popleft()
                if word == endWord:
                    return res
                # add neighbour to queue
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            # add element to that level
                            q.append(neiWord)
                            visit.add(neiWord)
            res += 1
        return 0
