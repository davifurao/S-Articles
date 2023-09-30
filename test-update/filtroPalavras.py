import re
from unidecode import unidecode

# Lista de preposições e artigos em português
# Função para carregar as palavras do arquivo de preposições
def carregar_preposicoes(arquivo_preposicoes):
    with open(arquivo_preposicoes, 'r', encoding='utf-8') as arquivo:
        preposicoes = [linha.strip() for linha in arquivo]
    return preposicoes

# Caminho para o arquivo de preposições
arquivo_preposicoes = './test-update/preposicoes.txt'#pasta para salvamento dos arquivos de preposições em pt_br

# Carregue as preposições do arquivo
preposicoes_pronomes = carregar_preposicoes(arquivo_preposicoes)
def filtro_de_palavras(arquivo_entrada, arquivo_saida):
    with open(arquivo_entrada, 'r', encoding='utf-8') as arquivo_entrada, open(arquivo_saida, 'w', encoding='utf-8') as arquivo_saida:
        for linha in arquivo_entrada:
            # Expressão regular para extrair palavras (removendo caracteres especiais e espaços)
            palavras_sem_preposicoes = re.findall(r'\b(?!' + '|'.join(preposicoes_pronomes) + r')\w+\b', linha, re.IGNORECASE)

            # Remover acentos e converter para minúsculas
            palavras_sem_preposicoes = [unidecode(palavra.lower()) for palavra in palavras_sem_preposicoes]

            # Ignorar palavras muito curtas (por exemplo, com menos de 3 letras) e palavras com números
            palavras_sem_preposicoes = [palavra for palavra in palavras_sem_preposicoes if len(palavra) > 2 and not any(c.isdigit() for c in palavra)]

            arquivo_saida.write(''.join(palavras_sem_preposicoes))




arquivo_entrada = './test-update/saida.txt'
arquivo_saida = './test-update/palavras_filtradas.txt'

filtro_de_palavras(arquivo_entrada, arquivo_saida)
