# Book Build Foods

Projeto para criar sistema web para gerenciar receitas de comida

## Tecnologias:

    - Python 3.10   
    - Django 4.1
    - PostgreSQL
    - venv
    - git
    - github workflow

## utilizando:

Para instalar as dependências:
    
```bash
$ pip install -r requirements.txt
```


para criar novo app

```bash
$ python manage.py startapp <nome_do_seu_app>
```


Para iniciar o projeto localmente na porta 8000:
```bash
$ python3 manage.py runserver
```

Para atualizar novos arquivos estáticos:

```bash
$ python3 manage.py collectstatic
```

Para criar a migração:

```bash
$ python manage.py makemigrations
```

Para criar as tabelas no banco:

```bash
$ python manage.py migrate
```



## Troubleshooting

Caso ocorra problema ao instalar o psycopg2 instale as dependências:
Lembrando que precisa do PostgreSQL instalando antes de instalar a dependência.

```bash
apt install libpq-dev python3-dev
```