# Kenzie Pet

Hi! I'm your first Markdown file in **StackEdit**. If you want to learn about StackEdit, you can read me. If you want to play with Markdown, you can edit me. Once you have finished with me, you can create new files by opening the **file explorer** on the left corner of the navigation bar.



# Este passo é para baixar o projeto

`git clone https://gitlab.com/<your_user>/kenzie_pet.git`

## Entrar na pasta

`cd kenzie_pet`

## Criar um ambiente virtual

`python3 -m venv venv`

## Entrar no ambiente virtual

`source venv/bin/activate`

## Instalar as dependências

`pip install -r requirements.txt`

## Criar o banco de dados

`./manage.py migrate`

## Rodar localmente

`./manage.py runserver`

Por padrão, irá rodar em `http://127.0.0.1:8000/`


# Rotas

The file explorer is accessible using the button in left corner of the navigation bar. You can create a new file by clicking the **New file** button in the file explorer. You can also create folders by clicking the **New folder** button.

### `GET /api/animals/`

Esta rota retorna todos os animais cadastrados no banco.

RESPONSE STATUS -> HTTP 200 (ok)

Response:
	

    [
      {
        "id": 1,
        "name": "Bidu",
        "age": 1.0,
        "weight": 30.0,
        "sex": "macho",
        "group": {
          "id": 1,
          "name": "cao",
          "scientific_name": "canis familiaris"
        },
        "characteristic_set": [
          {
            "id": 1,
            "characteristic": "peludo"
          },
          {
            "id": 2,
            "characteristic": "medio porte"
          }
        ]
      },
      {
        "id": 2,
        "name": "Hanna",
        "age": 1.0,
        "weight": 20.0,
        "sex": "femea",
        "group": {
          "id": 2,
          "name": "gato",
          "scientific_name": "felis catus"
        },
        "characteristic_set": [
          {
            "id": 1,
            "characteristic": "peludo"
          },
          {
            "id": 3,
            "characteristic": "felino"
          }
        ]
      }
    ]

### `GET /api/animals/<int:animal_id>/`

Esta rota retorna as informações do animal com id igual ao passado na rota.

RESPONSE STATUS -> HTTP 200 (ok)

    {
      "id": 1,
      "name": "Bidu",
      "age": 1.0,
      "weight": 30.0,
      "sex": "macho",
      "group": {
        "id": 1,
        "name": "cao",
        "scientific_name": "canis familiaris"
      },
      "characteristic_set": [
        {
          "id": 1,
          "characteristic": "peludo"
        },
        {
          "id": 2,
          "characteristic": "medio porte"
        }
      ]
    }

### `POST /api/animals/`

Esta rota é para a criação de informações de animais.

RESPONSE STATUS -> HTTP 201 (created)

Body:

    {
      "name": "Bidu",
      "age": 1,
      "weight": 30,
      "sex": "macho",
      "group": {
        "name": "cao",
        "scientific_name": "canis familiaris"
      },
      "characteristic_set": [
        {
          "characteristic": "peludo"
        },
        {
          "characteristic": "medio porte"
        }
      ]
    }

Response:

    {
      "id": 1,
      "name": "Bidu",
      "age": 1.0,
      "weight": 30.0,
      "sex": "macho",
      "group": {
        "id": 1,
        "name": "cao",
        "scientific_name": "canis familiaris"
      },
      "characteristic_set": [
        {
          "id": 1,
          "characteristic": "peludo"
        },
        {
          "id": 2,
          "characteristic": "medio porte"
        }
      ]
    }


### `DELETE /api/animals/<int:animal_id>/`

Rota para deletar as informações de um animal.

Não há conteúdo no retorno da requisição.

RESPONSE STATUS -> HTTP 204 (no content)


## Tecnologias utilizadas 📱

-   Django
-   Django Rest Framework
-   SQLite


## Licence

MIT
