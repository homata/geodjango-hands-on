```python
$ python -m venv env
$ source env/bin/activate
$ deactivate
$ pip install --upgrade pip
$ pip freeze

$ pip install django
$ pip install psycopg2-binary

$ pip install djangorestframework-gis
$ pip install django-filter
$ pip install markdown

$ pip freeze
    Django==2.0.6
    django-filter==1.1.0
    djangorestframework==3.8.2
    djangorestframework-gis==0.13
    Markdown==2.6.11
    psycopg2-binary==2.7.4
    pytz==2018.4
    six==1.11.0

$ pip freeze -l
$ pip freeze > requirements.txt
$ pip install -r requirements.txt
```

```

$ createdb -U postgres -E UTF-8 geodjangodb
$ psql -U postgres -d geodjangodb -c "CREATE EXTENSION postgis;"
$ psql -U postgres -d geodjangodb -c "select * from pg_available_extensions;"
$ psql -U postgres -l
```
 
```
$ python manage.py startapp world
$ python manage.py migrate
$ python manage.py createsuperuser
>>> Username (leave blank to use 'homata'): admin
>>> Email address: hoge@fuga.com
>>> Password: welcome123
>>> Password (again): welcome123
>>> Superuser created successfully.

$ python manage.py makemigrations
$ python manage.py migrate

```

```
$ python manage.py shell
>>> from world import load_hokkaido
>>> load_hokkaido.run()

>>> from world import load_elementary_school
>>> load_elementary_school.run()

>>> from world import load_public_facility
>>> load_public_facility.run()

>>> from world import load_busstop
>>> load_busstop.run()

>>> exit()
```
