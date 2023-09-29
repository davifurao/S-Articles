import subprocess # Para instalar o Flask caso não esteja instalado
import sys
import os
from werkzeug.utils import secure_filename

# Verificar se o Flask está instalado
try:
    import flask
except ImportError:
    print("O Flask não está instalado. Instalando...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Flask"])

# Usar o Flask para criar um servidor web
from flask import Flask, render_template, request, jsonify, send_from_directory, url_for
import json

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'  # Cria a pasta de uploads que salvará os arquivos enviados
ALLOWED_EXTENSIONS = {'pdf', 'txt'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Verificação de criação do arquivo de database
def criar_arquivo_database():
    if not os.path.exists('database.json'):
        # Se o arquivo não existir, crie-o com o conteúdo padrão
        with open('database.json', 'w') as file:
            data = {"artigos": []}
            json.dump(data, file, indent=4)
    else:
        try:
            # Tente abrir o arquivo e verificar seu conteúdo
            with open('database.json', 'r') as file:
                data = json.load(file)
            # Verifique se 'artigos' é uma lista
            if not isinstance(data.get('artigos'), list):
                # Se não for, substitua-o pelo conteúdo padrão
                data = {"artigos": []}
                with open('database.json', 'w') as file:
                    json.dump(data, file, indent=4)
        except (json.JSONDecodeError, FileNotFoundError):
            # Se ocorrer um erro ao carregar o arquivo, substitua-o pelo conteúdo padrão
            with open('database.json', 'w') as file:
                data = {"artigos": []}
                json.dump(data, file, indent=4)

# Chame a função para criar ou verificar o arquivo 'database.json'
criar_arquivo_database()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adicionar_artigo', methods=['POST'])
def adicionar_artigo():
    titulo = request.form['titulo']
    conteudo = request.form['conteudo']
    palavras_chave = request.form['palavrasChave'].split(',')
    categoria = request.form['categoria']

    arquivo = request.files['arquivo']  # Obter o arquivo enviado pelo formulário

    if arquivo and allowed_file(arquivo.filename):
        filename = secure_filename(arquivo.filename)
        arquivo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    else:
        return jsonify({"error": "Arquivo não suportado. Apenas PDF e TXT são permitidos."})

    with open('database.json', 'r') as file:
        data = json.load(file)

    novo_artigo = {
        "titulo": titulo,
        "conteudo": conteudo,
        "palavras_chave": palavras_chave,
        "categoria": categoria,
        "arquivo": filename  # Nome do arquivo no dicionário do artigo
    }

    data["artigos"].append(novo_artigo)

    with open('database.json', 'w') as file:
        json.dump(data, file, indent=4)

    return jsonify({"message": "Artigo adicionado com sucesso!"})

@app.route('/consultar_artigos', methods=['POST'])
def consultar_artigos():
    palavra_chave = request.json.get('palavraChave', '')

    with open('database.json', 'r') as file:
        data = json.load(file)

    artigos = data["artigos"]
    resultados = []

    for artigo in artigos:
        if palavra_chave in artigo['palavras_chave'] or palavra_chave in artigo['conteudo']:
            resultados.append(artigo)

    return jsonify(resultados)

@app.route('/exibir_artigo/<int:index>')
def exibir_artigo(index):
    with open('database.json', 'r') as file:
        data = json.load(file)
    
    artigos = data["artigos"]

    if index >= 0 and index < len(artigos):
        artigo = artigos[index]

        if 'arquivo' in artigo:
            arquivo_path = os.path.join(app.config['UPLOAD_FOLDER'], artigo['arquivo'])
            if os.path.exists(arquivo_path):
                artigo['arquivo_link'] = url_for('uploaded_file', filename=artigo['arquivo'])
            else:
                artigo['arquivo_link'] = None

        return jsonify(artigo)
    else:
        return jsonify({"error": "Índice fora dos limites da lista de artigos."})


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/uploads/<nome_do_arquivo>')
def servir_pdf(nome_do_arquivo):
    return send_from_directory('uploads', nome_do_arquivo)
if __name__ == '__main__':
    app.run(debug=True)
