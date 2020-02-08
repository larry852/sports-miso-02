# Colombia en Tokio 2020

## Deployment
- [Admin](https://sports-miso-02.herokuapp.com/)

## ERD
![ERD](doc/ERD.png?raw=true "ERD")

## API Endpoints

### General
| Endpoint | Parameters | Method | Response | Description | Token |
| --- | --- | --- | --- | --- | --- | 
| / |  | GET |  | Admin Django - WEB | <ul><li>[ ] </li></ul> |
| /api/v1/ |  | GET | <ul><li>CRUDs</li></ul> | Api root | <ul><li>[x] </li></ul> |

### Auth
| Endpoint | Parameters | Method | Response | Description | Token |
| --- | --- | --- | --- | --- | --- | 
| /api/v1/registration/ | <ul><li>user</li><li>organization id</li><li>role short name</li><li>phone number</li><li>place id</li></ul> | POST | <ul><li>key</li><li>user</li></ul> | Registration | <ul><li>[ ] </li></ul>
| /api/v1/registration/verify-email/ | <ul><li>key</li></ul> | POST | <ul><li>detail</li></ul> | Verify email | <ul><li>[ ] </li></ul> |
| /api/v1/login/ | <ul><li>email or username</li><li>password</li></ul> | POST | <ul><li>key</li><li>user</li></ul> | Login | <ul><li>[ ] </li></ul> |
| /api/v1/logout/ |  | POST | <ul><li>detail</li></ul> | Logout | <ul><li>[ ] </li></ul> |
| /api/v1/password/change/ | <ul><li>new_password1</li><li>new_password2</li><li>old_password</li></ul> | POST | <ul><li>detail</li></ul> | Change password | <ul><li>[x] </li></ul> |
| /api/v1/password/reset/ | <ul><li>email</li></ul> | POST | <ul><li>detail</li></ul> | Forgot password - send url -> /reset/uid/token/ | <ul><li>[ ] </li></ul> |
| /api/v1/password/reset/confirm/ | <ul><li>uid</li><li>token</li><li>new_password1</li><li>new_password2</li></ul> | POST | <ul><li>detail</li></ul> | Forgot password confirmation | <ul><li>[ ] </li></ul> |

### Current user
| Endpoint | Parameters | Method | Response | Description | Token |
| --- | --- | --- | --- | --- | --- | 
| /api/v1/user/ |  | GET | <ul><li>user</li></ul> | Get current user | <ul><li>[x] </li></ul> |
| /api/v1/user/ | <ul><li>user</li></ul> | PUT | <ul><li>user</li></ul> | Total update of current user | <ul><li>[x] </li></ul> |
| /api/v1/user/ | <ul><li>partial user</li></ul> | PATCH | <ul><li>user</li></ul> | Partial update of current user | <ul><li>[x] </li></ul> |


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
