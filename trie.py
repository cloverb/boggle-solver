class Node:
    """Node for use in Trie"""

    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    """Trie Implementation"""

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        """Insert word into trie"""
        current = self.root
        for letter in word:
            node = current.children.get(letter)
            if not node:
                current.children[letter] = Node()
            current = current.children[letter]
        current.is_word = True

    def search_word(self, word):
        """Check if given word is in trie"""
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            if not current:
                return False
        return current.is_word

    def search_prefix(self, prefix):
        """Check if given prefix is in trie"""
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if not current:
                return False
        return current.children
