class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndNode = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        
        curr_node = self.root
        for c in word:
            if not c in curr_node.children:
                curr_node.children[c] = TrieNode()
            curr_node = curr_node.children[c]
        curr_node.isEndNode = True
    
    def search(self, word: str) -> bool:
        
        curr_node = self.root
        for c in word:
            if not c in curr_node.children:
                return False
            curr_node = curr_node.children[c]
        return curr_node.isEndNode

    def startsWith(self, prefix: str) -> bool:
        
        curr_node = self.root
        for c in prefix:
            if not c in curr_node.children:
                return False
            curr_node = curr_node.children[c]
        return True