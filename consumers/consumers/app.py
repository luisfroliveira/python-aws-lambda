from chalice import Chalice

app = Chalice(app_name='consumers')

# Dados de exemplo para usuários e empresas
users = {
    "users": [
        {"name": "usuário1", "phone": "47999999999"},
        {"name": "usuário2", "phone": "47999999999"},
        {"name": "usuário3", "phone": "47999999999"},
    ]
}

companies = {
    "companies": [
        {"name": "empresa1", "telefone": "47999999999"},
        {"name": "empresa2", "telefone": "47999999999"},
        {"name": "empresa3", "telefone": "47999999999"},
    ]
}

# Endpoint para criar um usuário
@app.route('/consumers/person', methods=['POST'])
def create_user():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Usuário {requests_params} criado com sucesso!"
    }
    return response

# Endpoint para atualizar um usuário
@app.route('/consumers/person', methods=['PUT'])
def update_user():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Usuário {requests_params} atualizado com sucesso!"
    }
    return response

# Endpoint para deletar um usuário
@app.route('/consumers/person', methods=['DELETE'])
def delete_user():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Usuário {requests_params} deletado com sucesso!"
    }
    return response

# Endpoint para obter a lista de usuários
@app.route('/consumers/persons', methods=['GET'])
def get_persons():
    response = {
        "statusCode": 200,
        "body": users
    }
    return response

# Endpoint para obter um usuário específico com base no ID
@app.route('/consumers/person/{id}', methods=['GET'])
def get_person(id):
    response = {
        "statusCode": 200,
        "body": {id: {"name": "usuário1", "telefone": "47999999999"}}
    }
    return response

# Endpoint para criar uma empresa
@app.route('/consumers/company', methods=['POST'])
def create_company():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Empresa {requests_params} criada com sucesso!"
    }
    return response

# Endpoint para atualizar uma empresa
@app.route('/consumers/company', methods=['PUT'])
def update_company():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Empresa {requests_params} atualizada com sucesso!"
    }
    return response

# Endpoint para deletar uma empresa
@app.route('/consumers/company', methods=['DELETE'])
def delete_company():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Empresa {requests_params} deletada com sucesso!"
    }
    return response

# Endpoint para obter a lista de empresas
@app.route('/consumers/companies', methods=['GET'])
def get_companies():
    response = {
        "statusCode": 200,
        "body": companies
    }
    return response

# Endpoint para obter uma empresa específica com base no ID
@app.route('/consumers/company/{id}', methods=['GET'])
def get_company(id):
    response = {
        "statusCode": 200,
        "body": {id: {"name": "empresa1", "telefone": "47999999999"}}
    }
    return response
