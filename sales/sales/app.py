from chalice import Chalice

app = Chalice(app_name='sales')

# Dicionário de vendas
sales = {
            "sales": [
                {"consumer": "usuário1", "value": "12,50", "food": "pizza"},
                {"consumer": "usuário2", "value": "11,80", "food": "estrogonofe"},
                {"consumer": "usuário3", "value": "10,90", "food": "macarronada"},
            ]
        }

# Rota para criar uma venda offline
@app.route('/sales/offline', methods = ['POST'])
def create_sale():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Venda {requests_params} criada com sucesso!"
    }
    return response

# Rota para atualizar uma venda offline
@app.route('/sales/offline',  methods=['PUT'])
def update_sale():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Venda {requests_params} atualizada com sucesso!"
    }
    return response

# Rota para excluir uma venda offline
@app.route('/sales/offline',  methods=['DELETE'])
def delete_sale():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Venda {requests_params} deletada com sucesso!"
    }
    return response

# Rota para obter todas as vendas offline
@app.route('/sales/offlines',  methods=['GET'])
def get_sales():
    response = {
        "statusCode": 200,
        "body": sales
    }
    return response

# Rota para obter uma venda offline específica pelo id
@app.route('/sales/offline/{id}',  methods=['GET'])
def get_sale(id):
    response = {
        "statusCode": 200,
        # Retorna uma venda fixa, independentemente do id fornecido
        "body": {id: {"consumer": "usuário1", "value": "12,50", "food": "pizza"}}
    }
    return response

# Rota para criar uma venda online
@app.route('/sales/online',  methods=['POST'])
def create_sale():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Venda {requests_params} criada com sucesso!"
    }
    return response

# Rota para atualizar uma venda online
@app.route('/sales/online',  methods=['PUT'])
def update_sale():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Venda {requests_params} atualizada com sucesso!"
    }
    return response

# Rota para excluir uma venda online
@app.route('/sales/online',  methods=['DELETE'])
def delete_sale():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Venda {requests_params} deletada com sucesso!"
    }
    return response

# Rota para obter todas as vendas online
@app.route('/sales/onlines',  methods=['GET'])
def get_sales():
    response = {
        "statusCode": 200,
        # Retorna o mesmo dicionário de vendas, independentemente de serem vendas online ou offline
        "body": sales
    }
    return response

# Rota para obter uma venda online específica pelo id
@app.route('/sales/online/{id}',  methods=['GET'])
def get_sale(id):
    response = {
        "statusCode": 200,
        # Retorna uma venda fixa, independentemente do id fornecido e independentemente de ser uma venda online ou offline
        "body": {id: {"consumer": "usuário1", "value": "12,50", "food": "<EUGPSCoordinates>"}}
    }
    return response
