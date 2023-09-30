import re
from unidecode import unidecode

class FiltroPalavras:
    
    def __init__(self):
        arquivo_preposicoes = f'test-update-encapsulated/filter_word/arquivo_preposicoes.txt'# PAY ATTENTION TO THIS LINE(DIRECTORY)
        self.preposicoes_pronomes = self.carregar_preposicoes(arquivo_preposicoes)

    # Função para carregar as palavras do arquivo de preposições
    def carregar_preposicoes(self, arquivo_preposicoes):
        with open(arquivo_preposicoes, 'r', encoding='utf-8') as arquivo:
            preposicoes = [linha.strip() for linha in arquivo]
        return preposicoes

    def filtrar_palavras(self, arquivo_entrada, arquivo_saida):
        with open(arquivo_entrada, 'r', encoding='utf-8') as arquivo_entrada, open(arquivo_saida, 'w', encoding='utf-8') as arquivo_saida:
            for linha in arquivo_entrada:
                # Expressão regular para extrair palavras (removendo caracteres especiais e espaços)
                palavras_sem_preposicoes = re.findall(r'\b(?!' + '|'.join(self.preposicoes_pronomes) + r')\w+\b', linha, re.IGNORECASE)

                # Remover acentos e converter para minúsculas
                palavras_sem_preposicoes = [unidecode(palavra.lower()) for palavra in palavras_sem_preposicoes]

                # Ignorar palavras muito curtas (por exemplo, com menos de 3 letras) e palavras com números
                palavras_sem_preposicoes = [palavra for palavra in palavras_sem_preposicoes if len(palavra) > 2 and not any(c.isdigit() for c in palavra)]

                arquivo_saida.write(''.join(palavras_sem_preposicoes))
