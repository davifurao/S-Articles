import subprocess
from pdfminer.high_level import extract_text
import re

# Comando para instalar o PDFMiner (se necessário)
comando_instalacao = "pip install pdfminer.six"

# Execute o comando de instalação (se necessário)
try:
    subprocess.run(comando_instalacao, shell=True, check=True)
    print("Biblioteca PDFMiner instalada com sucesso.")
except subprocess.CalledProcessError as e:
    print(f"Erro ao instalar a biblioteca PDFMiner: {e}")

# Função para converter PDF em texto e remover caracteres indesejados
def pdf_para_txt_com_preprocessamento(pdf_path, txt_path):
    # Extraia o texto do PDF
    texto = extract_text(pdf_path)

    # pré processamento 
    texto = re.sub(r'\x0C', '', texto)

    # Laço de escrita para o texto pré processado
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(texto)

    print(f'Conversão concluída. Texto extraído para {txt_path}')

# NPUT e OUTPUT do arquivo
pdf_file = './test-update/DAVI_SOUZA_DE_LUNA_certificado_expotec_2023_20230921151414.pdf'#Arquivo no mesmo diretório
txt_file = './test-update/saida.txt'

pdf_para_txt_com_preprocessamento(pdf_file, txt_file)# Chamada da função
