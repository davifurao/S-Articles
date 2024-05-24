import json
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
            
    def read_other_file(self, file_name):
        try:
            with open(file_name, 'r') as arquivo:
                texto = arquivo.read()
            return texto
        except FileNotFoundError:
            print(f"O arquivo '{file_name}' não foi encontrado.")
            return None
        except Exception as e:
            print(f"Ocorreu um erro ao ler o arquivo '{file_name}': {e}")
            return None
    
    #É o que eu quero usar       
    def save_json(self, data, novo_arquivo=None):
        if novo_arquivo is None:
            novo_arquivo = self.file_name

        try:
            # Converter conjuntos em listas antes de serializar em JSON, porque JSON não suporta conjuntos  
            data_serializavel = []
            for palavra, arquivos in data:
                data_serializavel.append((palavra, list(arquivos)))

            with open(novo_arquivo, 'w') as arquivo:
                json.dump(data_serializavel, arquivo)
            print(f"Os dados foram salvos em formato JSON no arquivo '{novo_arquivo}'.")
        except Exception as e:
            print(f"Ocorreu um erro ao salvar os dados em formato JSON no arquivo '{novo_arquivo}': {e}")


#print(texto)

trie = PrefixeTrie.PrefixTrie()

def insert(texto, arquive_name):
    for palavra in texto.split():
        trie.insert(palavra, str(arquive_name))

#insert("texto","saida.txt")
print(trie.list_palavras())

#esse é um teste de busca
palavra = "ensolarada"
if trie.search(palavra):
    print(f"A palavra '{palavra}' está presente na árvore.")
else:
    print(f"A palavra '{palavra}' não está presente na árvore.")
  
#Nome do arquivo JSON para salvar os dados da árvore  
read_save = readSaveData("trie.json")

#Vou ler de um arquivo diferente
saida = read_save.read_other_file("saida.txt")

#inserrir na arvore
insert(saida, "saida.txt")

#debug
print(trie.list_palavras())

#Operação de salvamento
read_save.save_json(trie.list_palavras())


