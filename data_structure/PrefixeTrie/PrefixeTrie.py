class PrefixTrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class PrefixTrie:
    def __init__(self):
        self.root = PrefixTrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = PrefixTrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        
    def remove(self, word):
        def _remove_helper(node, word, depth):
            if depth == len(word):
                if node.is_end_of_word:
                    node.is_end_of_word = False
                    if not node.children:  # Se o nó não tiver filhos, ele pode ser removido
                        del node
                        return True
                return False

            char = word[depth]
            if char in node.children and _remove_helper(node.children[char], word, depth + 1):
                if not node.children[char].children:  # Se o filho não tiver filhos, ele pode ser removido
                    del node.children[char]
                    return not node.is_end_of_word  # Retorna True se este nó não for o final de uma palavra
            return False

        _remove_helper(self.root, word, 0)

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def _list_words(self, node, prefix, words):
        if node.is_end_of_word:
            words.append(prefix)
        for char, child_node in node.children.items():
            self._list_words(child_node, prefix + char, words)

    def list_words(self):
        words = []
        self._list_words(self.root, "", words)
        return words


