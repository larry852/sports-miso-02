# sports-miso-02

## Run
```sh
git clone https://github.com/larry852/sports-miso-02
cd sports-miso-02
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt

python manage.py runserver
```

## Run
```sh
cd sports-miso-02
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```