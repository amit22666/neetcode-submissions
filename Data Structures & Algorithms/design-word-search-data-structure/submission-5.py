class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, s: str) -> bool:
            if not s:                    # no chars left
                return node.word
            c, rest = s[0], s[1:]
            if c == ".":
                for child in node.children.values():
                    if dfs(child, rest):
                        return True
                return False
            else:
                if c not in node.children:
                    return False
                return dfs(node.children[c], rest)

        return dfs(self.root, word)
