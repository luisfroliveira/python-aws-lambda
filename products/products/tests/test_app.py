# Importando o módulo Client do Chalice para testes
from chalice.test import Client
# Importando a instância do aplicativo Chalice criado no arquivo 'app.py'
from app import app
# Importando o módulo json para manipulação de dados JSON
import json

# Teste para criar um novo produto
def test_create_product():
    # Criando uma instância do cliente de teste usando o aplicativo Chalice
    with Client(app) as client:
        # Simulando uma solicitação HTTP POST para a rota '/product'
        response = client.http.post(
            '/product',
            body=json.dumps({"product": "arroz", "amount": "2"}),
            headers={"Content-Type": "application/json"}
        )
        # Exibindo a resposta do servidor (aqui, apenas para fins de depuração)
        print(response.json_body)
        # Verificando se a resposta tem o status code 200 (OK)
        assert response.json_body["statusCode"] == 200

# Teste para atualizar um produto existente
def test_update_product():
    # Criando uma instância do cliente de teste usando o aplicativo Chalice
    with Client(app) as client:
        # Simulando uma solicitação HTTP PUT para a rota '/product'
        response = client.http.put(
            '/product',
            body=json.dumps({"product": "arroz", "amount": "2"}),
            headers={"Content-Type": "application/json"}
        )
        # Exibindo a resposta do servidor (aqui, apenas para fins de depuração)
        print(response.json_body)
        # Verificando se a resposta tem o status code 200 (OK)
        assert response.json_body["statusCode"] == 200

# Teste para excluir um produto existente
def test_delete_product():
    # Criando uma instância do cliente de teste usando o aplicativo Chalice
    with Client(app) as client:
        # Simulando uma solicitação HTTP DELETE para a rota '/product'
        response = client.http.delete(
            '/product',
            body=json.dumps({"product": "arroz", "amount": "2"}),
            headers={"Content-Type": "application/json"}
        )
        # Exibindo a resposta do servidor (aqui, apenas para fins de depuração)
        print(response.json_body)
        # Verificando se a resposta tem o status code 200 (OK)
        assert response.json_body["statusCode"] == 200

# Teste para obter todos os produtos
def test_get_products():
    # Criando uma instância do cliente de teste usando o aplicativo Chalice
    with Client(app) as client:
        # Simulando uma solicitação HTTP GET para a rota '/products'
        response = client.http.get('/products')
        # Exibindo a resposta do servidor (aqui, apenas para fins de depuração)
        print(response.json_body)
        # Verificando se a resposta tem o status code 200 (OK)
        assert response.json_body["statusCode"] == 200

# Teste para obter um produto específico
def test_get_product():
    # Criando uma instância do cliente de teste usando o aplicativo Chalice
    with Client(app) as client:
        # Simulando uma solicitação HTTP GET para a rota '/product/1'
        response = client.http.get('/product/1')
        # Exibindo a resposta do servidor (aqui, apenas para fins de depuração)
        print(response.json_body)
        # Verificando se a resposta tem o status code 200 (OK)
        assert response.json_body["statusCode"] == 200
