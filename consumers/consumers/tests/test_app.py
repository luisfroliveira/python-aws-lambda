from chalice.test import Client
from app import app
import json

# Teste para criar um usuário
def test_create_person():
    with Client(app) as client:
        response = client.http.post(
            '/consumers/person',
            body=json.dumps({"name": "usuário1", "phone": "47999999999"}),
            headers={"Content-Type": "application/json"}
        )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

# Teste para atualizar um usuário
def test_update_person():
    with Client(app) as client:
        response = client.http.put(
            '/consumers/person',
            body=json.dumps({"name": "usuário1", "phone": "47999999999"}),
            headers={"Content-Type": "application/json"}
        )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

# Teste para deletar um usuário
def test_delete_person():
    with Client(app) as client:
        response = client.http.delete(
            '/consumers/person',
            body=json.dumps({"name": "usuário1", "phone": "47999999999"}),
            headers={"Content-Type": "application/json"}
        )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

# Teste para obter a lista de usuários
def test_get_persons():
    with Client(app) as client:
        response = client.http.get(
            '/consumers/persons'
        )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

# Teste para obter um usuário específico com base no ID
def test_get_person():
    with Client(app) as client:
        response = client.http.get(
            '/consumers/person/1'
        )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

# Teste para criar uma empresa
def test_create_company():
    with Client(app) as client:
        response = client.http.post(
            '/consumers/company',
            body=json.dumps({"name": "empresa1", "telefone": "47999999999"}),
            headers={"Content-Type": "application/json"}
        )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

# Teste para atualizar uma empresa
def test_update_company():
    with Client(app) as client:
        response = client.http.put(
            '/consumers/company',
            body=json.dumps({"name": "empresa1", "telefone": "47999999999"}),
            headers={"Content-Type": "application/json"}
        )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

# Teste para deletar uma empresa
def test_delete_company():
    with Client(app) as client:
        response = client.http.delete(
            '/consumers/company',
            body=json.dumps({"name": "empresa1", "telefone": "47999999999"}),
            headers={"Content-Type": "application/json"}
        )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

# Teste para obter a lista de empresas
def test_get_companies():
    with Client(app) as client:
        response = client.http.get(
            '/consumers/companies'
        )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

# Teste para obter uma empresa específica com base no ID
def test_get_company():
    with Client(app) as client:
        response = client.http.get(
            '/consumers/company/1'
        )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200