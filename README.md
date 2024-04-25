BACKEND

Создаем виртуальное окружение и запускаем его следующими командами:

python3 -m venv venv

source venv/bin/activate

Переходим в папку с бэкэндом:

cd cookingbook

и устанавливаем requirements:

python -m pip install -r requirements.txt

Запускаем бэкэнд проекта:

python manage.py runserver


FRONTEND (отдельно открываем папку frontend):

В папке frontend создаем свое виртуальное окружение и запускаем его:

python3 -m venv env

source env/bin/activate

Устанавливаем Axios для корректной работы:

sudo npm install axios

Запускаем клиентскую часть проекта на React:
sudo npm start
