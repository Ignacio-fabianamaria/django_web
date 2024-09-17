
### Explicação dos Comandos

1. **`pip install virtualenv`**: Instala o pacote `virtualenv`, que permite criar ambientes virtuais Python.

2. **`python3 -m venv cadastro_curso_womakers`**: Cria um ambiente virtual chamado `cadastro_curso_womakers`.

3. **`source cadastro_curso_womakers/bin/activate`**: Ativa o ambiente virtual. No Windows, o comando é diferente (`cadastro_curso_womakers\Scripts\activate`).

4. **`pip install django`**: Instala o Django no ambiente virtual.

5. **`django-admin startproject projeto_womakers .`**: Cria um novo projeto Django chamado `projeto_womakers` no diretório atual.

6. **`python3 manage.py startapp base`**: Cria uma nova aplicação dentro do projeto Django chamada `base`.

7. **`python3 manage.py runserver`**: Inicia o servidor de desenvolvimento do Django para que você possa visualizar o projeto no navegador.

8. **`python manage.py makemigrations`**: Gera arquivos de migração para refletir alterações nos modelos do Django.

9. **`python manage.py migrate`**: Aplica as migrações ao banco de dados para atualizar seu esquema.

10. **`python manage.py createsuperuser`**: Cria um superusuário para acessar o painel administrativo do Django.

