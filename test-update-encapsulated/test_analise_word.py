from filter_word import ConversorPDF, FiltroPalavras

filtro = FiltroPalavras()
convert = ConversorPDF()

arquivo_pdf = './test-update-encapsulated/DAVI_SOUZA_DE_LUNA_certificado_expotec_2023_20230921151414.pdf'
arquivo_txt_convertido = './test-update-encapsulated/arquivo_txt.txt'

convert.pdf_para_txt_com_preprocessamento(arquivo_pdf, arquivo_txt_convertido)

arquivo_entrada = arquivo_txt_convertido 
arquivo_saida = './test-update-encapsulated/arquivo_saida.txt'

filtro.filtrar_palavras(arquivo_entrada, arquivo_saida)


