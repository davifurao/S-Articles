import subprocess
from pdfminer.high_level import extract_text
import re

class ConversorPDF:
    def __init__(self):
        # Comando para instalar o PDFMiner (se necessário)
        comando_instalacao = "pip install pdfminer.six"

        # Execute o comando de instalação (se necessário)
        try:
            subprocess.run(comando_instalacao, shell=True, check=True)
            print("Biblioteca PDFMiner instalada com sucesso.")
        except subprocess.CalledProcessError as e:
            print(f"Erro ao instalar a biblioteca PDFMiner: {e}")

    # Função para converter PDF em texto e remover caracteres indesejados
    def pdf_para_txt_com_preprocessamento(self, pdf_path, txt_path):
        # Extraia o texto do PDF
        texto = extract_text(pdf_path)

        # Pré-processamento
        texto = re.sub(r'\x0C', '', texto)

        # Laço de escrita para o texto pré-processado
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(texto)

        print(f'Conversão concluída. Texto extraído para {txt_path}')
