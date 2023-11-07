
# API de Usuários com FastAPI

Esta é uma API de usuários simples criada com FastAPI. Ela permite realizar operações básicas de CRUD (Create, Read, Update, Delete) em recursos de usuário. Você pode usar esta API para criar, recuperar, atualizar e excluir informações de usuário.
## Pré-requisitos

Antes de começar a usar esta API, você precisará instalar todas as dependências listadas no arquivo `requirements.txt` usando o seguinte comando:

```bash
pip install -r requirements.txt
```


## Executando a API

Execute o seguinte comando no terminal para iniciar a API:

```bash
uvicorn main:app --reload
```

Isso iniciará o servidor FastAPI na porta padrão (8000) com recarregamento automático.


## Rotas da API

####  Retorna a lista de todos os usuários:

```http
  GET /api/v1/users
```


#### Retorna as informações de um usuário específico:

```http
  GET /api/v1/users/{id}
```

#### Cria um novo usuário com base nos dados fornecidos no corpo da solicitação:

```http
  POST /api/v1/users
```

#### Atualiza as informações de um usuário existente com base no ID fornecido:

```http
  PUT /api/v1/users/{id}
```

#### Exclui um usuário com base no ID fornecido:

```http
  DELETE /api/v1/users/{id}
```




## Documentação

A API é fornecida com documentação interativa gerada automaticamente. Você pode acessá-la em http://localhost:8000/docs após iniciar a API. A documentação fornece informações detalhadas sobre todas as rotas, parâmetros e exemplos de uso.

## Exemplo de uso

Aqui está um exemplo de como você pode usar a API com Python e a biblioteca requests:

```python
import requests

# URL base da API
base_url = 'http://localhost:8000'

# Lista de usuários
response = requests.get(f'{base_url}/api/v1/users')
print(response.json())

# Criar um novo usuário
new_user = {'first_name': 'João', 'last_name': 'Silva', 'gender': 'male', 'roles': 'user'}
response = requests.post(f'{base_url}/api/v1/users', json=new_user)
print(response.json())

# Atualizar informações de um usuário
user_id = "08aa225e-4df2-4560-b245-31bb2d35401c""
updated_data = {'first_name': 'Novo Nome'}
response = requests.put(f'{base_url}/api/v1/users/{user_id}', json=updated_data)
print(response.json())

# Excluir um usuário
user_id = "08aa225e-4df2-4560-b245-31bb2d35401c"
response = requests.delete(f'{base_url}/api/v1/users/{user_id}')
print(response.json())
```
