
### ⚙️ Comandos Utilizados

#### 🔹 Cadastro

1. **`pip install virtualenv`**: Instala o pacote `virtualenv`, que permite criar ambientes virtuais Python.

2. **`python3 -m venv cadastro_curso_womakers`**: Cria um ambiente virtual chamado `cadastro_curso_womakers`.

3. **`source cadastro_curso_womakers/bin/activate`**: Ativa o ambiente virtual. No Windows, o comando é diferente (`cadastro_curso_womakers\Scripts\activate`).

4. **`pip install django`**: Instala o Django no ambiente virtual.

5. **`django-admin startproject projeto_womakers .`**: Cria um novo projeto Django chamado `projeto_womakers` no diretório atual.

6. **`python3 manage.py startapp base`**: Cria uma nova aplicação dentro do projeto Django chamada `base`.

7. **`python3 manage.py runserver`**: Inicia o servidor de desenvolvimento do Django para que você possa visualizar o projeto no navegador.

8. **`python3 manage.py makemigrations`**: Gera arquivos de migração para refletir alterações nos modelos do Django.

9. **`python3 manage.py migrate`**: Aplica as migrações ao banco de dados para atualizar seu esquema.

10. **`python3 manage.py createsuperuser`**: Cria um superusuário para acessar o painel administrativo do Django.


#### 🔹 Cursos

1. **`python3 manage.py startapp cursos`**: Cria uma nova aplicação chamada cursos dentro do projeto Django.

#### 🔹 Rest_API

1. **`pip install djangorestframework`**: Instala o Django REST Framework, que permite construir APIs robustas no Django.

2. **`python manage.py startapp rest_ap`**: Cria uma nova aplicação chamada rest_api dentro do projeto Django

#### Testes de API

pip install pytest-django

criar na raiz do projeto o arquivo pytest.ini com a seguinte config:

 ``` bash
 [pytest]
DJANGO_SETTINGS_MODULE = projeto_womakers.settings
python_files = tests.py test_*.py *_test.py

```