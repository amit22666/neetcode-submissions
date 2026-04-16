class TrieNode():
    def __init__(self):
        self.children = {}
        self.IsEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.IsEndOfWord = True
        

    
    def search(self, word: str) -> bool:
        def dfs(node, word):
            if not word:
                return node.IsEndOfWord
            c = word[0]
            if c == '.':
                for child in node.children.values():
                    if dfs(child, word[1:]):
                        return True
                return False
            else:
                if c not in node.children:
                    return False
                return dfs(node.children[c],word[1:])
        return dfs(self.root, word)
