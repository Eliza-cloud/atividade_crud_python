from flask import Flask, jsonify, request 

app = Flask(__name__) 

produtos = [ 
  
    {
        'id': 1,
        'nome': 'celular',
        'preco': 400
    },

   {
       'id': 2,
       'nome': 'notebook',
       'preco': 500
   },

   {
        'id': 3,
        'nome': 'televisão',
        'preco': 250
   },
   {
       'id': 4,
       'nome': 'fone de ouvido',
       'preco': 70
   }
]

#Função com a rota para retornar usarios da api
@app.route('/produtos', methods=['GET'])
def consultar_produtos():
    return jsonify(produtos)

@app.route('/produtos/<int:id>', methods=['GET'])
def consultar_por_id(id):
    for produto in produtos:
     if produto.get('id') == id: 
      return jsonify(produto)

@app.route('/produtos', methods= ['POST'])
def cadastrar_produtos():
   novo_produto = request.get_json()
   produtos.append(novo_produto)
   return jsonify(produtos)

@app.route('/produtos/<int:id>', methods= ['PUT'])
def atualizar_por_id(id): 
  atualizar_produto = request.get_json()
  for indice,produto in enumerate(produtos):
     if produto.get ('id') == id:
        produtos[indice].update(atualizar_produto)
        return jsonify(produtos[indice])
     

@app.route('/produtos/<int:id>', methods=['DELETE'])
def excluir_produto_por_id(id):
   for indice,produto in enumerate(produtos):
      if produto.get('id') == id:
        del produtos[indice]
        return jsonify(produto) 
    
        
      
app.run(port=8080,host='localhost',debug=True)


