class PrefixTrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.arquivos = set()  # Conjunto para armazenar os nomes dos arquivos associados à palavra

class PrefixTrie:
    def __init__(self):
        self.root = PrefixTrieNode()

    def insert(self, palavra, arquivo):
        node = self.root
        for char in palavra:
            if char not in node.children:
                node.children[char] = PrefixTrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.arquivos.add(arquivo)  # Adiciona o nome do arquivo à lista de arquivos associados à palavra

    def remove(self, palavra):
        def _remove_helper(node, palavra, depth):
            if depth == len(palavra):
                if node.is_end_of_word:
                    node.is_end_of_word = False
                    if not node.children:  # Se o nó não tiver filhos, ele pode ser removido
                        del node
                        return True
                return False

            char = palavra[depth]
            if char in node.children and _remove_helper(node.children[char], palavra, depth + 1):
                if not node.children[char].children:  # Se o filho não tiver filhos, ele pode ser removido
                    del node.children[char]
                    return not node.is_end_of_word  # Retorna True se este nó não for o final de uma palavra
            return False

        _remove_helper(self.root, palavra, 0)

    def search(self, palavra):
        node = self.root
        for char in palavra:
            if char not in node.children:
                return None  # Retorna None se a palavra não for encontrada na árvore
            node = node.children[char]
        if node.is_end_of_word:
            return node.arquivos  # Retorna os nomes dos arquivos associados à palavra
        else:
            return None  # Retorna None se a palavra não for uma palavra completa na árvore

    def _list_palavras(self, node, prefix, palavras):
        if node.is_end_of_word:
            palavras.append((prefix, node.arquivos))  # Adiciona a palavra e os arquivos associados à lista de palavras
        for char, child_node in node.children.items():
            self._list_palavras(child_node, prefix + char, palavras)

    def list_palavras(self):
        palavras = []
        self._list_palavras(self.root, "", palavras)
        return palavras
