class TrieNode:
    def __init__(self, char):
        self.children = {}
        self.is_end = False
        self.child_hash = ""
        self.char = char

class Trie:
    def __init__(self):
        self.root = TrieNode("/")
        self.hashmap = collections.defaultdict(int)
        self.duplicates = []

    def insert(self, folder):
        current_node = self.root
        for char in folder:
            if char not in current_node.children:
                current_node.children[char] = TrieNode(char)
            current_node = current_node.children[char]
        current_node.is_end = True

    def _hash_children(self, root):
        for char in sorted(root.children.keys()):
            self._hash_children(root.children[char])
            root.child_hash += char + '|' + root.children[char].child_hash + '|' 
        self.hashmap[root.child_hash] += 1
    
    def hash_children(self):
        current_node = self.root
        self._hash_children(current_node)
    
    def _get_duplicates(self, root, path):
        if root.children and self.hashmap[root.child_hash] > 1: 
            return
        self.duplicates.append(path + [root.char])
        for char in root.children:
            self._get_duplicates(root.children[char], path + [root.char])

    def get_duplicates(self):
        current_node = self.root
        for char in current_node.children:
            self._get_duplicates(current_node.children[char], [])
        return self.duplicates

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        trie = Trie()
        for path in paths:
            trie.insert(path)
        trie.hash_children()
        return trie.get_duplicates()
