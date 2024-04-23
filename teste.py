import re
from unidecode import unidecode

# Função para carregar as preposições do arquivo de preposições
def carregar_preposicoes(arquivo_preposicoes):
    with open(arquivo_preposicoes, 'r', encoding='utf-8') as arquivo:
        preposicoes = [linha.strip() for linha in arquivo]#tira as linhas em branco e etc do arquivo de preposição
    return preposicoes

# Função para filtrar palavras do arquivo de entrada e escrever no arquivo de saída
def filtro_de_palavras(arquivo_entrada, arquivo_saida, preposicoes_pronomes):
    with open(arquivo_entrada, 'r', encoding='utf-8') as arquivo_entrada, open(arquivo_saida, 'w', encoding='utf-8') as arquivo_saida:
        for linha in arquivo_entrada:
            # Expressão regular para extrair palavras (removendo caracteres especiais e espaços)
            palavras = re.findall(r'\b\w+\b', linha)

            # Remover preposições e pronomes
            palavras_sem_preposicoes = [palavra for palavra in palavras if palavra.lower() not in preposicoes_pronomes]

            # Escrever as palavras no arquivo de saída, separadas por espaço e com quebra de linha no final
            arquivo_saida.write(' '.join(palavras_sem_preposicoes) + '\n')

# Caminho para o arquivo de preposições
arquivo_preposicoes = './prepositions_pronouns/pt-br/preposicoes_pronomes.txt'

# Carregar as preposições do arquivo
preposicoes_pronomes = carregar_preposicoes(arquivo_preposicoes)#engraçado que a tipagem do arquivo ne é definida kkkk

# Arquivo de entrada e saída
arquivo_entrada = './entrada.txt'
arquivo_saida = './saida.txt'

# chamada da função de filtrar palavras
filtro_de_palavras(arquivo_entrada, arquivo_saida, preposicoes_pronomes)
