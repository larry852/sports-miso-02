# sports-miso-02

## Initial configuration

```sh
git clone https://github.com/larry852/sports-miso-02
cd sports-miso-02
virtualenv -p python3 env
```

## Run

```sh
cd sports-miso-02
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## ???

```sh
python manage.py startapp polls
```

## How to know which components my app have ?

```sh
pip freeze
pip freeze > requirements.txt
```

## Run migrations for specific databases

Remember:
1. Create an empty "sports" database if you are using postgres.
2. Follow [this link](https://stackoverflow.com/a/47845784) if you have troubles with PostgreSQL connection.

### Connections

* "default" --> Connect to local SQLite3 database
* "postgres" --> Connect to postgres database
* "heroku" --> Connect to postgres database in Heroku

Examples:

*To run migrations in local SQLite3 database*
```sh
python manage.py migrate
```

*To run migrations in local postgres database*
```sh
python manage.py migrate --database=postgres
```

*To run migration in Heroku postgres database*
```sh
python manage.py migrate --database=heroku
```
