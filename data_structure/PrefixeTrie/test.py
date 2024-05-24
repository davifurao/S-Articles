import PrefixeTrie

def test():
    trie = PrefixeTrie.PrefixTrie() # PrefixTrie é a classe que implementa a Trie e PrefixeTrie é o arquivo que contém a classe, cuidado com isso para não confundir. Um possui o "e" , já o outro não.
    trie.insert("apple")
    trie.insert("app")
    trie.insert("ap")
    trie.insert("banana")
    trie.insert("band")
    trie.insert("bandana")
    trie.insert("bandit")
    list(trie)
    print("removendo apple...")
    trie.remove("apple")
    list(trie)




def list(trie):
    print(trie.list_words())
    
test()