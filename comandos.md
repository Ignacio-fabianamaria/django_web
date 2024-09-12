
pip install virtualenv

python3 -m venv cadastro_curso_womakers

source cadastro_curso_womakers/bin/activate

pip install django

django-admin startproject projeto_womakers .

python3 manage.py startapp base

python3 manage.py runserver

