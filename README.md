# 🏆 League of Legends Build Manager

Um projeto em **Python + FastAPI** para gerenciar e consultar **campeões
e builds** de *League of Legends*. O sistema é dividido em dois
módulos: - 🖥️ **Servidor (API REST)** --- Gerencia os dados dos campeões
e suas builds. - 💡 **Cliente (Interface CLI)** --- Permite interagir
com o servidor via terminal.

------------------------------------------------------------------------

## 📂 Estrutura do Projeto

    project/
    │
    ├── client/
    │   └── main.py          # Interface CLI (cliente que consome a API)
    │
    ├── server/
    │   ├── server.py        # Servidor FastAPI
    │   └── dados/
    │       └── champions.json  # Base de dados dos campeões
    │
    ├── requirements.txt     # Lista de dependências do projeto
    └── README.md

------------------------------------------------------------------------

## ⚙️ Requisitos

-   **Python 3.10+**
-   **FastAPI**
-   **Uvicorn**
-   **Requests**

Instale as dependências com:

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## 🚀 Executando o Projeto

### 1️⃣ Inicie o servidor

No diretório `server/`, execute:

``` bash
uvicorn server:app --reload
```

Por padrão, o servidor será iniciado em:

    http://127.0.0.1:8000

------------------------------------------------------------------------

### 2️⃣ Inicie o cliente

No diretório `client/`, execute:

``` bash
python main.py
```

O cliente exibirá um menu no terminal para interagir com a API:

    ==================================================
    |X|X|X| CAMPEÕES DO LEAGUE OF LEGENDS |X|X|X|
    1-Listar todos os campeões
    2-Listar um campeão
    3-Inserir build em um campeão
    4-Pesquisar build por campeão
    0-Sair

------------------------------------------------------------------------

## 🧠 Funcionalidades

### 🧾 1. Listar todos os campeões

Exibe todos os campeões disponíveis no arquivo `champions.json`.

**Endpoint:**\
`GET /champion/all`

------------------------------------------------------------------------

### 🔍 2. Pesquisar campeão

Exibe informações de um campeão específico (id e título).

**Endpoint:**\
`GET /champion/{nome}`

------------------------------------------------------------------------

### 🧰 3. Inserir build

Permite adicionar uma build (6 itens) para um campeão existente.

**Endpoint:**\
`POST /champion/{nome}/build`

**Exemplo de corpo JSON enviado:**

``` json
{
  "item1": "Força da Trindade",
  "item2": "Dança da Morte",
  "item3": "Placa Gargolítica",
  "item4": "Cutelo Negro",
  "item5": "Hidra Raivosa",
  "item6": "Anjo Guardião"
}
```

**Resposta esperada:**

``` json
{
  "message": "Build inserida com sucesso!",
  "build": {
    "id": 1,
    "item1": "Força da Trindade",
    "item2": "Dança da Morte",
    "item3": "Placa Gargolítica",
    "item4": "Cutelo Negro",
    "item5": "Hidra Raivosa",
    "item6": "Anjo Guardião"
  }
}
```

------------------------------------------------------------------------

### 🧩 4. Visualizar builds de um campeão

Retorna uma build específica de um campeão (pelo ID da build).

**Endpoint:**\
`GET /champion/{nome}/build{id}`

**Exemplo:**

    GET /champion/Garen/build1

------------------------------------------------------------------------

## 💾 Estrutura do Banco de Dados (`champions.json`)

Exemplo de estrutura do arquivo:

``` json
{
  "data": {
    "Garen": {
      "id": "Garen",
      "title": "O Poder de Demacia",
      "build": [
        {
          "id": 1,
          "item1": "Força da Trindade",
          "item2": "Placa Gargolítica",
          "item3": "Dança da Morte",
          "item4": "Cutelo Negro",
          "item5": "Capa de Fogo Solar",
          "item6": "Anjo Guardião"
        }
      ]
    },
    "Ahri": {
      "id": "Ahri",
      "title": "A Raposa de Nove Caudas",
      "build": []
    }
  }
}
```

------------------------------------------------------------------------

## ⚠️ Tratamento de Erros

A API retorna erros padronizados em formato JSON.\
Exemplo de resposta ao buscar um campeão inexistente:

``` json
{
  "detail": "Esse campeão não existe."
}
```

No cliente, isso é exibido como:

    ERRO: Esse campeão não existe.

------------------------------------------------------------------------

## 🧑‍💻 Tecnologias Utilizadas

-   **Python 3**
-   **FastAPI** → criação do servidor REST\
-   **Uvicorn** → servidor ASGI\
-   **Requests** → consumo da API no cliente\
-   **JSON** → armazenamento e leitura de dados

------------------------------------------------------------------------

## 🌟 Possíveis Melhorias Futuras

-   Adicionar autenticação de usuários.\
-   Implementar atualização e exclusão de builds.\
-   Criar interface web com FastAPI + HTML/CSS.\
-   Integrar com a API oficial do League of Legends.

------------------------------------------------------------------------

## 👨‍🏫 Autores

**Mateus Grandel**\
**Arthur A. Leite**\
💻 Projeto criado para estudo de **APIs REST com FastAPI e Python.**
