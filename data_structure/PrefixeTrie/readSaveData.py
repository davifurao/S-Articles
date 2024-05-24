import PrefixeTrie


class readSaveData:
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        try:
            with open(self.file_name, 'r') as arquivo:
                texto = arquivo.read()
            return texto
        except FileNotFoundError:
            print(f"O arquivo '{self.file_name}' não foi encontrado.")
            return None
        except Exception as e:
            print(f"Ocorreu um erro ao ler o arquivo '{self.file_name}': {e}")
            return None
    #caso precise salvar outro tipo de arquivo, é só e qualquer outro método configurar corretamente para o tipo de arquivo
    def save(self, texto, novo_arquivo=None):
        if novo_arquivo is None:
            novo_arquivo = self.file_name

        try:
            with open(novo_arquivo, 'w') as arquivo:
                arquivo.write(texto)
            print(f"Os dados foram salvos no arquivo '{novo_arquivo}'.")
        except Exception as e:
            print(f"Ocorreu um erro ao salvar os dados no arquivo '{novo_arquivo}': {e}")
    
    #É o que eu quero usar       
    def save_json(self, data, novo_arquivo=None):
        if novo_arquivo is None:
            novo_arquivo = self.file_name

        try:
            with open(novo_arquivo, 'w') as arquivo:
                json.dump(data, arquivo)
            print(f"Os dados foram salvos em formato JSON no arquivo '{novo_arquivo}'.")
        except Exception as e:
            print(f"Ocorreu um erro ao salvar os dados em formato JSON no arquivo '{novo_arquivo}': {e}")


#print(texto)

trie = PrefixeTrie.PrefixTrie()

def insert(texto):
    for palavra in texto.split():
        trie.insert(palavra)

insert(texto)
print(trie.list_words())

palavra = "ensolarada"
if trie.search(palavra):
    print(f"A palavra '{palavra}' está presente na árvore.")
else:
    print(f"A palavra '{palavra}' não está presente na árvore.")


