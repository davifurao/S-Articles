function consultarArtigos() {
    var palavraChave = document.getElementById('consultaPalavraChave').value;

    // Use a função fetch para enviar a solicitação POST ao servidor Flask
    fetch('/consultar_artigos', {
        method: 'POST',
        body: JSON.stringify({ palavraChave: palavraChave }), // Envie os dados como JSON
        headers: {
            'Content-Type': 'application/json', // Especifique o tipo de conteúdo JSON
        }
    })
    .then(response => response.json())
    .then(resultados => {
        var listaArtigos = document.getElementById('listaArtigos');
        listaArtigos.innerHTML = ''; // Limpa a lista atual

        if (resultados.length === 0) {
            // Se não houver correspondência, exiba a mensagem
            var mensagem = document.createElement('p');
            mensagem.textContent = 'Não existe correspondência.';
            listaArtigos.appendChild(mensagem);
        } else {
            // Exibe os resultados como links clicáveis
            resultados.forEach(function (artigo, index) {
                var link = document.createElement('a');
                link.href = '#';
                link.textContent = artigo.titulo;
                link.onclick = function () {
                    exibirConteudoArtigo(index);
                };
                var listItem = document.createElement('li');
                listItem.appendChild(link);
                listaArtigos.appendChild(listItem);
            });
        }
    });

    return false; // Para evitar que o formulário seja enviado
}
function abrirPDF(nomeArquivo) {
    var url = '/uploads/' + nomeArquivo;
    window.open(url, '_blank');
}

function exibirConteudoArtigo(index) {
    fetch(`/exibir_artigo/${index}`)
        .then(response => response.json())
        .then(artigo => {
            var conteudoArtigo = document.getElementById('conteudoArtigo');
            conteudoArtigo.innerHTML = '';

            var titulo = document.createElement('h3');
            titulo.textContent = artigo.titulo;

            var conteudo = document.createElement('p');
            conteudo.textContent = artigo.conteudo;

            var palavrasChave = document.createElement('p');
            palavrasChave.textContent = 'Palavras-chave: ' + artigo.palavras_chave.join(', ');

            var categoria = document.createElement('p');
            categoria.textContent = 'Categoria: ' + artigo.categoria;

            // Verifica se o artigo possui um arquivo PDF associado
            if (artigo.arquivo) {
                var abrirPDFButton = document.createElement('button');
                abrirPDFButton.textContent = 'Abrir PDF';
                abrirPDFButton.onclick = function () {
                    abrirPDF(artigo.arquivo);
                };
                conteudoArtigo.appendChild(abrirPDFButton);
            }

            conteudoArtigo.appendChild(titulo);
            conteudoArtigo.appendChild(conteudo);
            conteudoArtigo.appendChild(palavrasChave);
            conteudoArtigo.appendChild(categoria);
        });
}


