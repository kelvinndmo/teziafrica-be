
make freeze:
	pip freeze > requirements.txt

make install:
	pip install -r requirements.txt
  
make migrations:
	python3 manage.py makemigrations

make migrate:
	python3 manage.py migrate

make server:
	python3 manage.py runserver

make freeze:
	pip freeze > requirements.txt


make superuser:
	python3 manage.py createsuperuser
