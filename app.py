from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
            {
                "autor": "Miguel Luis Resende",
                "id": 1,
                "titulo": "Teste 1"
            },
            {
                "autor": "Matheus Henrique",
                "id": 2,
                "titulo": "Teste 2"
            },
            {
                "autor": "Colleen Hoover",
                "id": 4,
                "titulo": "É Assim que Acaba: 1"
            },
        ]


# Consulta (todos)
@app.route('/livros')
def obterLivros(): 
    return jsonify(livros)

# Consulta (id)
@app.route('/livros/<int:id>', methods = ['GET'])
def obter_livro_por_ID(id):
    for livro in livros:
       if livro.get('id') == id:
           return jsonify(livro)

# Editar
@app.route('/livros/<int:id>', methods = ['PUT'])
def editar_livro_por_Id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

# Criar novo livro
@app.route('/livros', methods = ['POST'])
def criar_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(novo_livro)

# Excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]  
    return jsonify(livros)
    
    
app.run(port=5000,host='localhost',debug=True)