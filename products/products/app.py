# Importando o módulo Chalice
from chalice import Chalice

# Criando uma instância do aplicativo Chalice com o nome 'products'
app = Chalice(app_name='products')

# Definindo uma estrutura de dados que contém informações sobre produtos
products = {
    "products": [
        {"product": "arroz", "amount": "2"},
        {"product": "feijão", "amount": "3"},
        {"product": "carne", "amount": "1"},
    ]
}

# Rota para criar um novo produto usando o método HTTP POST
@app.route('/product', methods=['POST'])
def create_product():
    # Obtendo os parâmetros do corpo da solicitação (JSON)
    requests_params = app.current_request.json_body
    # Criando uma resposta com status 200 e mensagem de sucesso
    response = {
        "statusCode": 200,
        "body": f"Produto {requests_params} criado com sucesso!"
    }
    return response

# Rota para atualizar um produto existente usando o método HTTP PUT
@app.route('/product', methods=['PUT'])
def update_product():
    # Obtendo os parâmetros do corpo da solicitação (JSON)
    requests_params = app.current_request.json_body
    # Criando uma resposta com status 200 e mensagem de sucesso
    response = {
        "statusCode": 200,
        "body": f"Produto {requests_params} atualizado com sucesso!"
    }
    return response

# Rota para excluir um produto existente usando o método HTTP DELETE
@app.route('/product', methods=['DELETE'])
def delete_product():
    # Obtendo os parâmetros do corpo da solicitação (JSON)
    requests_params = app.current_request.json_body
    # Criando uma resposta com status 200 e mensagem de sucesso
    response = {
        "statusCode": 200,
        "body": f"Produto {requests_params} deletado com sucesso!"
    }
    return response

# Rota para obter todos os produtos usando o método HTTP GET
@app.route('/products', methods=['GET'])
def get_products():
    # Criando uma resposta com status 200 e retornando a estrutura de dados 'products'
    response = {
        "statusCode": 200,
        "body": products
    }
    return response

# Rota para obter um produto específico usando o método HTTP GET e passando um parâmetro 'id'
@app.route('/product/{id}', methods=['GET'])
def get_product(id):
    # Criando uma resposta com status 200 e retornando um produto específico com base no 'id'
    response = {
        "statusCode": 200,
        "body": {id: {"product": "arroz", "amount": "2"}}
    }
    return response
