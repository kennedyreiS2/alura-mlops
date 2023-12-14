# Alura API

[![Python versions](https://img.shields.io/badge/python-3.11.x-blue.svg)](https://www.python.org/downloads/release/python-3116/)

Organização do Projeto
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

### Índice

- [Requisitos](#requisitos)
- [Executando o projeto](#executando-o-projeto)
    - [Criando ambiente virtual e instalando as dependências](#criando-ambiente-virtual-e-instalando-as-dependências)
    - [Executando em desenvolvimento](#executando-em-desenvolvimento)
    - [Executando em produção](#executando-em-produção)
    - [Executando com Docker](#executando-com-docker)
- [Documentação das rotas](#documentação-das-rotas)
- [Referências](#referências)


### Requisitos

-  **Python 3.11.x** - O interpretador está disponível para download [aqui](https://www.python.org/)
    - Verifique a versão instalada digitando:
         ```bash
         $ python --version
        ```

### Executando o projeto

Existem duas formas de executar o projeto, sendo em ambiente local de desenvolvimento e ambiente de produção.

 - Independente da forma escolhida, o primeiro passa é clonar o repositório

1. Clone o repositório:

    ```bash
    $ git clone <url_repositorio>
    $ cd <diretorio_criado>
    ```

#### Criando ambiente virtual e instalando as dependências

1. Crie um *virtual environment* (certifique-se que a versão do python em sua máquina é igual ou superior a 3.11):

    ```bash
    $ python3.11 -m venv venv
    ```

2. Ative o ambiente e instale os pacotes via `pip` no *virtual environment*:

    ```bash
    #comando de ativação no Linux/macOS
    $ source venv/bin/activate

    #comando de ativação no windows
    $ ./venv/Scripts/activate

    #comando de instalação dos pacotes
    (venv) $ pip install -r requirements.txt
    ```

#### Executando em desenvolvimento

1. Crie uma cópia do arquivo *_.env.example_*  dê o nome de *_.env_* e preencha os valores corretos para as variáveis de ambiente.

2. Execute o comando de execução do Flask:

```bash
flask run
```

#### Executando em produção [em construção]

#### Executando com Docker [em construção]

### Documentação das rotas [em construção]

<details><summary><code><b>/verify</b></code></summary>

#### Rota responsável por verificar o status da API (healthcheck).

**URL** : `/verify`

**Method** : `GET`

**Auth required** : NO

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "message": "api está no ar"
}
```

</details>

<details><summary><code><b>/users</b></code></summary>

#### Rota responsável pela criação dos usuários.

**URL** : `/users`

**Method** : `POST`

**Auth required** : NO

**Modelo de dados**

Deve ser passado o email e a senha para se criar um novo usuário.

```json
{
    "email": "[string format email]",
    "password": "[string]"
}
```

**Exemplo de dados** Todos os campos devem ser enviados.

```json
{
    "email": "teste@email.com",
    "password": "senha1234"
}
```

## Success Response

**Condição** : Se todos os campos estiverem corretos, e um usuário com o email enviado ainda não existir, será criado um novo usuário.

**Code** : `201 CREATED`

**Content example**

```json
{
    "_id": "asdf123123",
    "email": "teste@email.com"
}
```

## Error Responses

**Condição** : Se uma conta já existe.

**Code** : `409 CONFLICT`

**Content example**

```json
{
    "message": "Email já existe"
}
```

### Or

**Condição** : Se o email enviado estiver no formato incorreto.

**Code** : `400 BAD REQUEST`

**Content example**

```json
{
    "email": "<invalid_email> is not email"
}
```

</details>

<details><summary><code><b>/login</b></code></summary>

#### Rota responsável pela criação do JWT (login).

**URL** : `/login`

**Method** : `POST`

**Auth required** : NO

**Modelo de dados**

Deve ser passado o email e a senha para fazer o login.

```json
{
    "email": "[string format email]",
    "password": "[string]"
}
```

**Exemplo de dados** Todos os campos devem ser enviados.

```json
{
    "email": "teste@email.com",
    "password": "senha1234"
}
```

## Success Response

**Condição** : Se todos os campos estiverem corretos, o email estiver no formato válido, o usuário existir e a senha estiver correta, é retornado um JWT.

**Code** : `201 CREATED`

**Content example**

```json
{
    "token": "laksdjflasidjlkajsdjhasdfhaklsjdfhkaljsdh...",
}
```

## Error Responses

**Condição** : Usuário ou senha inválidas.

**Code** : `401 UNAUTHORIZED`

**Content example**

```json
{
    "message": "Email ou senha inválidos"
}
```

### Or

**Condição** : Se o email enviado estiver no formato incorreto.

**Code** : `400 BAD REQUEST`

**Content example**

```json
{
    "email": "<invalid_email> is not email"
}
```

</details>

<details><summary><code><b>/tables</b></code></summary>

#### Rota responsável pela busca de dados no databricks.

**URL** : `/tables`

**Method** : `GET`

**Auth required** : YES

**Headers** :
- Authorization: `Bearer <JWT>`

**Query params** Filtros usados na listagem dos dados

**Obrigatórios** :
- **name** : Nome da tabela do deltasharing
- **share** : Nome do endpoint do deltasharing
- **schema** : Nome da camada do deltasharing

**Opcionais** :
- **limit** : Quantidade máxima de linhas buscadas
- **columns** : Nome das colunas a serem exibidas
- **filter** : Filtragem de dados baseado em uma única coluna

**Exemplo de query_params** :

- **name** : cs_creditos
- **share** : customer360
- **schema** : gold
- **limit** : 100
- **columns** : ID_CLIENTE,SCORE
- **filter** : ID_CLIENTE=0000012345

Os parâmetros listados acima são parâmetros de query, e a URL ficará da seguinte forma ao ser enviada na requisição:
`/tables?name=cs_creditos&share=customer360&schema=gold&limit=100&COLUMNS=ID_CLIENTE,SCORE&filter=ID_CLIENTE=0000000103`

## Success Response

**Condição** : Se os dados do deltasharing estiverem corretos, os parâmtros opcionais forem enviados no padrão exemplificado e o dados filtrado existir, então será retornado o dado buscado.

**Code** : `200 OK`

**Content example**

```json
[
  {
    "ID_CLIENTE": "0000012345",
    "SCORE": 1.0
  }
]
```

## Error Responses

**Condição** : Parâmetros de name, share ou schema incorretos.

**Code** : `404 NOT FOUND`

**Content example**

```json
{
    "message": "Tabelas não encontradas no databricks, verifique se os parâmetros'name', 'share' e 'schema' estão corretos."
}
```

### Or

**Condição** : Se o valor enviada em `columns` não existir.

**Code** : `400 BAD REQUEST`

**Content example**

```json
{
    "message": "Coluna(s) ['COLUNA_ERRADA'] não identificada(s) no Databricks",
    "valid_columns": [
        "ID_CLIENTE",
        "SCORE",
        "VALE_CREDITO",
        "VALOR_BONUS"
  ]
}
```

### Or

**Condição** : Se o valor enviado em `filter` não encontrar nenhum dado.

**Code** : `404 NOT FOUND`

**Content example**

```json
{
    "message": "Dados não encontrados"
}
```

</details>

#### Referências

- https://www.digitalocean.com/community/tutorials/how-to-setup-a-firewall-with-ufw-on-an-ubuntu-and-debian-cloud-server#before-we-get-started
- https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04#step-6-%E2%80%94-securing-the-application

---
###### Copyright © 2023 [Kennedy Reis](kennedyreis.m@gmail.com) - All rights reserved.

[![Python-powered](https://github.com/allexlima/nMail/blob/master/aux/imgs/PythonPoweredAnimSmall.gif?raw=true)](https://www.python.org/)
