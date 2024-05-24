import PrefixeTrie

trie = PrefixeTrie.PrefixTrie() # PrefixTrie é a classe que implementa a Trie e PrefixeTrie é o arquivo que contém a classe, cuidado com isso para não confundir. Um possui o "e" , já o outro não.

def test():
    trie.insert("apple","saida.txt")
    trie.insert("app","saida.txt")
    trie.insert("ap","saida.txt")
    trie.insert("banana","saida.txt")
    trie.insert("band","saida.txt")
    trie.insert("bandana","saida.txt")
    trie.insert("bandit","saida.txt")
    list(trie)
    print("removendo apple...")
    trie.remove("apple")
    list(trie)
    




def list(trie):
    print(trie.list_palavras())
    
test()
list(trie)

palavra = "banana"
arquivos_associados = trie.search(palavra)
if arquivos_associados:
    print(f"Os arquivos associados à palavra '{palavra}' são: {arquivos_associados}")
else:
    print(f"A palavra '{palavra}' não foi encontrada na árvore.")