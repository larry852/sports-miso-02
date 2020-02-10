# Colombia en Tokio 2020 - Backend

* Application built in Python using DJango.
* Configured to be depoyed in Heroku.

## Deployment
[Admin](https://sports-miso-02.herokuapp.com/)

## ERD
![ERD](doc/ERD.png?raw=true "ERD")

## API Endpoints

### General
| Endpoint | Description | Token |
| --- | --- | --- | 
| / | Admin Django - WEB | <ul><li>[ ] </li></ul> |
| /api/v1/ | Api root | <ul><li>[x] </li></ul> |

### Auth
| Endpoint | Description | Token |
| --- | --- | --- | 
| /api/v1/registration/ | Registration | <ul><li>[ ] </li></ul>
| /api/v1/login/  | Login | <ul><li>[ ] </li></ul> |
| /api/v1/logout/ | Logout | <ul><li>[ ] </li></ul> |
| /api/v1/password/change/ | Change password | <ul><li>[x] </li></ul> |
| /api/v1/password/reset/ | Forgot password - send url -> /reset/uid/token/ | <ul><li>[ ] </li></ul> |
| /api/v1/password/reset/confirm/ | Forgot password confirmation | <ul><li>[ ] </li></ul> |

### Current user
| Endpoint | Description | Token |
| --- | --- | --- | 
| /api/v1/user/ | Get current user | <ul><li>[x] </li></ul> |
| /api/v1/user/ | Total update of current user | <ul><li>[x] </li></ul> |
| /api/v1/user/ | Partial update of current user | <ul><li>[x] </li></ul> |

## Requirements

```sh
sudo apt install python3
sudo apt install python-pip
sudo pip install virtualenv
sudo apt install python3-dev
sudo apt install libpq-dev
```

## Run first time

```sh
git clone https://github.com/larry852/sports-miso-02
cd sports-miso-02
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

## Update migrations, packages and run

```sh
cd sports-miso-02
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Create apps

```sh
python manage.py startapp xxx
```

Replace the "xxx" value for the module name.

## How to know which components my app have ?

```sh
pip freeze
pip freeze > requirements.txt
```

## Run migrations for specific databases

Remember:
1. Create an empty "sports" database if you are using postgres.
2. Follow [this link](https://stackoverflow.com/a/47845784) if you have troubles with PostgreSQL connection.

### Set up the default database

Set this environment variable in your local:

```sh
export DJANGO_DATABASE="xxx"
```

Replace the "xxx" value for:

* "postgres" --> Connect to local postgres database.
* "heroku" --> Connect to postgres database in Heroku.

If you don't set the "DJANGO_DATABASE", the "default" database is going to be the local SQLite3 database.
