from chalice.test import Client
from app import app
import json

# Teste para criar uma venda offline
def test_create_offline():
    with Client(app) as client:
        # Envia uma solicitação POST para a rota /sales/offline com um corpo JSON contendo os dados da venda
        response = client.http.post(
                        '/sales/offline',
                        body=json.dumps({"consumer": "usuário1", "value": "12,50", "food": "pizza"}),
                        headers={"Content-Type": "application/json"}
                    )
        # Imprime o corpo da resposta JSON para depuração
        print(response.json_body)
        # Verifica se o código de status da resposta é 200, indicando sucesso
        assert response.json_body["statusCode"] == 200

# Teste para atualizar uma venda offline
def test_update_offline():
    with Client(app) as client:
        # Envia uma solicitação PUT para a rota /sales/offline com um corpo JSON contendo os dados da venda
        response = client.http.put(
                        '/sales/offline',
                        body=json.dumps({"consumer": "usuário1", "value": "12,50", "food": "pizza"}),
                        headers={"Content-Type": "application/json"}
                    )
        # Imprime o corpo da resposta JSON para depuração
        print(response.json_body)
        # Verifica se o código de status da resposta é 200, indicando sucesso
        assert response.json_body["statusCode"] == 200

# Teste para excluir uma venda offline
def test_delete_offline():
    with Client(app) as client:
        # Envia uma solicitação DELETE para a rota /sales/offline com um corpo JSON contendo os dados da venda
        response = client.http.delete(
                        '/sales/offline',
                        body=json.dumps({"consumer": "usuário1", "value": "12,50", "food": "pizza"}),
                        headers={"Content-Type": "application/json"}
                    )
        # Imprime o corpo da resposta JSON para depuração
        print(response.json_body)
        # Verifica se o código de status da resposta é 200, indicando sucesso
        assert response.json_body["statusCode"] == 200

# Teste para obter todas as vendas offline
def test_get_offlines():
    with Client(app) as client:
        # Envia uma solicitação GET para a rota /sales/offlines
        response = client.http.get(
                        '/sales/offlines'
                    )
        # Imprime o corpo da resposta JSON para depuração
        print(response.json_body)
        # Verifica se o código de status da resposta é 200, indicando sucesso
        assert response.json_body["statusCode"] == 200

# Teste para obter uma venda offline específica pelo id
def test_get_offline():
    with Client(app) as client:
        # Envia uma solicitação GET para a rota /sales/offline/1
        response = client.http.get(
                        '/sales/offline/1'
                    )
        # Imprime o corpo da resposta JSON para depuração
        print(response.json_body)
        # Verifica se o código de status da resposta é 200, indicando sucesso
        assert response.json_body["statusCode"] == 200

# Teste para criar uma venda online
def test_create_online():
    with Client(app) as client:
        # Envia uma solicitação POST para a rota /sales/online com um corpo JSON contendo os dados da venda
        response = client.http.post(
                        '/sales/online',
                        body=json.dumps({"consumer": "usuário1", "value": "12,50", "food": "pizza"}),
                        headers={"Content-Type": "application/json"}
                    )
        # Imprime o corpo da resposta JSON para depuração
        print(response.json_body)
        # Verifica se o código de status da resposta é 200, indicando sucesso
        assert response.json_body["statusCode"] == 200

# Teste para atualizar uma venda online
def test_update_online():
    with Client(app) as client:
        # Envia uma solicitação PUT para a rota /sales/online com um corpo JSON contendo os dados da venda
        response = client.http.put(
                        '/sales/online',
                        body=json.dumps({"consumer": "usuário1", "value": "12,50", "food": "<EUGPSCoordinates>"}),
                        headers={"Content-Type": "application/json"}
                    )
        # Imprime o corpo da resposta JSON para depuração
        print(response.json_body)
        # Verifica se o código de status da resposta é 200, indicando sucesso
        assert response.json_body["statusCode"] == 200

# Teste para excluir uma venda online
def test_delete_online():
    with Client(app) as client:
        # Envia uma solicitação DELETE para a rota /sales/online com um corpo JSON contendo os dados da venda
        response = client.http.delete(
                        '/sales/online',
                        body=json.dumps({"consumer": "usuário1", "value": "12,50", "food": "pizza"}),
                        headers={"Content-Type": "application/json"}
                    )
        # Imprime o corpo da resposta JSON para depuração
        print(response.json_body)
        # Verifica se o código de status da resposta é 200, indicando sucesso
        assert response.json_body["statusCode"] == 200

# Teste para obter todas as vendas online
def test_get_onlines():
    with Client(app) as client:
        # Envia uma solicitação GET para a rota /sales/onlines
        response = client.http.get(
                        '/sales/onlines'
                    )
        # Imprime o corpo da resposta JSON para depuração
        print(response.json_body)
        # Verifica se o código de status da resposta é 200, indicando sucesso
        assert response.json_body["statusCode"] == 200

# Teste para obter uma venda online específica pelo id
def test_get_online():
    with Client(app) as client:
        # Envia uma solicitação GET para a rota /sales/online/1
        response = client.http.get(
                        '/sales/online/1'
                    )
        # Imprime o corpo da resposta JSON para depuração
        print(response.json_body)
        # Verifica se o código de status da resposta é 200, indicando sucesso
        assert response.json_body["statusCode"] == 200
