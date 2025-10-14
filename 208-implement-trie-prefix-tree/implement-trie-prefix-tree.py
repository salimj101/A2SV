class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None ] * 26

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        
        node = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_end = True

    def search(self, word: str) -> bool:
        
        node = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        
        node = self.root
        for char in prefix:
            idx = ord(char) - ord('a')
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)