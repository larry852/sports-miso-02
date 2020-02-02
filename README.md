# sports-miso-02

## 

### Requirements
```sh
sudo apt install python3
sudo apt install python-pip
sudo pip install virtualenv
sudo apt install python3-dev
sudo apt install libpq-dev
```

## Run fisrt time
```sh
git clone https://github.com/larry852/sports-miso-02
cd sports-miso-02
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt

python manage.py runserver
```
## Create apps
```sh
python manage.py startapp polls
```

## Update migrations, packages and run
```sh
cd sports-miso-02
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
