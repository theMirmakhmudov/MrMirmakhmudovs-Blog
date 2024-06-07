makemig:
	python3 manage.py makemigrations

mig:
	python3 manage.py migrate
admin:
	python3 manage.py createsuperuser

run:
	python3 manage.py runserver