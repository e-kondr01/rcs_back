# Django backend for RCS ITMO.
by Egor Kondrashov, 2021.

При деплое нужно прописать следующие команды:
sudo chown -R 777:777 ./logs
sudo chown -R 777:777 ./rcs_back/media

Т. к. это mounted папки, в которые хотят писать приложения внутри докера.
Но они работают не от root, а от пользователя 777:777.

git clone https://github.com/xalvaine/restarter.git
фронт

Gunicorn workers на сервере иногда умирали с signal 9, скорее всего
потому что не хватало памяти. Пофиксил, добавив swap-memory.


ТЕСТИРОВАНИЕ


run tests:
python manage.py test --settings config.settings.test --parallel --keepdb


coverage: 

coverage run manage.py test --settings config.settings.test --parallel --keepdb

coverage html

смотрим htmlcov/index.html


SSL

добавил через certbot по этой статье: https://pentacent.medium.com/nginx-and-lets-encrypt-with-docker-in-less-than-5-minutes-b4b8a60d3a71

Однако скрипт из неё не работал, так что сделал вручную по шагам то, что он делает