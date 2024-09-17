# django_web

# Como Iniciar o Projeto

Siga os passos abaixo para configurar e rodar o projeto Django localmente na sua máquina.

## 1. Clonar o Repositório

Primeiro, clone o repositório para o seu ambiente local e acesse o diretório do projeto:

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_PROJETO>

```

## 2. Criar e Ativar o Ambiente Virtual

```bash
python3 -m venv cadastro_curso_womakers

```

## 3. Para ativar o ambiente virtual

No Windows:

```bash
cadastro_curso_womakers\Scripts\activate

```

No Linux/macOS:

```bash
source cadastro_curso_womakers/bin/activate

```

## 4.Instalar as Dependências

```bash
pip install -r requirements.txt

```

## 5.Iniciar o servidor

```bash
python3 manage.py runserver

```

## 6. Configurar o Banco de Dados
Sempre que houver alterações nos modelos do Django, execute os seguintes comandos para configurar o banco de dados:

- Gerar arquivos de migração:

```bash
python manage.py makemigrations

```

- Aplicar as migrações ao banco de dados:

```bash
python manage.py migrate

```

## 7. Criar um Superusuário
Para acessar o painel administrativo do Django, crie um superusuário:

```bash
python manage.py createsuperuser

```



# Em Construção 🚧