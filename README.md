# Бэкенд CRM-системы для Амбассадоров Яндекс Практикума.

## Команда:

- Роман [@rsaleksandrov](https://t.me/rsaleksandrov);
- Михаил [@greenpandorik](https://t.me/greenpandorik);
- Никита [@Rederickmind](https://t.me/Rederickmind);
- Дмитрий [@DimaC1985](https://t.me/DimaC1985).

## Стек технологий:

- **Python**
  - python 3.10
- **Разработка** (requirements.txt)
    - django 4.2.7
    - djangorestframework
    - drf-yasg
    - psycopg2-binary 2.9.9
    - gunicorn 21.2.0
    - python-dotenv 1.0.1
- **Стилизация** (requirements_style.txt)
    - black
    - isort
    - flake8
    - pep8-naming
    - flake8-broken-line
    - flake8-return
    - flake8-isort
- **Дополнительно** (для развертывания/деплоя)
    - docker
    - docker compose
    - PostgreSQL (docker image)
    - Nginx (docker image)

## Установка для разработки

1. Клонируем репозиторий https://github.com/Praktikum-Am-CRM/backend
2. Переходим в папку с проектом и создаем виртуальное окружение
    ```shell
    python -m venv venv
    ```
3. Активируем ВО
   - Windows
     ```shell 
     .\venv\Scripts\activate
     ```
   - Linux/Mac
     ```shell
     source ./venv/bin/activate
     ```
4. Обновляем `pip`, устанавливаем зависимости
   ```shell
   python.exe -m pip install --upgrade pip
   pip install -r requirements.txt
   ```
   Для поддержания стилистики устанавливаем
   ```shell
   pip install -r requirements_style.txt
   ```
5. В папке `infra` создаем файл `.env`. Образец заполнения в файле `example.
   env`.
   - Настройки django:
     - `ALOWED_HOSTS` - список хостов, на которых может запускаться проект. В обазятельном порядке указываются `django` и IP или доменное имя хоста, на котором развернут сервер. Хосты указываются через запятую, без http  и портов
     - `CSRF_TRUSTED_ORIGINS` - список доверенных хостов, с которых могут приходить запросф. В обазятельном порядке указываются `django` и IP или доменное имя хоста, на котором развернут сервер. Хосты указываются через запятую, с указанием протокола (http://, https://)  и порта. 
     - `SECRET_KEY` - буквенно-цифровая последовательность для шифрования (буквы - английские)
     - `ENGINE` - механизм, который используется для поключения к БД. В данном проекте должно быть равно `django.db.backends.postgresql`
     - `DEBUG` - если указано `True`, то при ошибках выводится отладочная информация, если `False` - выводится просто ошибка сервера
     - `POSTGRES_DB` - если указано `True`, используется PostgreSQL, если `False` - SQLite
   - Настройки для подключения к БД:
     - `POSTGRES_DB` - имя БД
     - `POSTGRES_HOST` - хост, на котором располагается БД. В данном проекте - `postgres`
     - `POSTGRES_PORT` - порт подключения к БД. В данном проекте - `5432`
     - `POSTGRES_USER` - имя пользователя для подключения к БД
     - `POSTGRES_PASSWORD` - пароль для подключения к БД
6. Запуск
    - в отладочном режиме
      ```shell
      python manage.py runserver
      ```
6. ...

### Запуск с использованием докера

В папке `infra` расположены два файла для запуска докер контейнеров:
- `docker-compose-local.yml` - для полноценного развертывания в "боевую" 
  систему. Поднимает контейнеры `postgres` (БД), `django` (собственно 
  бэкенд) и `nginx` (http сервер)
- `docker-compose-postgres-only.yml` - поднимает только контейнер `postgres` 
  (БД)

> **ВАЖНО:** Для работы с использованием контейнеров в файле `.env` надо 
установить `POSTGRES_DB=True`. В противном случае даже в контейнере будет 
использоваться SQLite.

Для запуска контейнеров переходим в папку `infra` и выполняем команду
```shell
docker compose --file <имя соответствующего yml файла> up --build
```

Если нужен запуск в режиме демона, то в конце добавляем ключ `-d`.
Для Linux (и скорее всего Mac) в начале указываем команду `sudo`

### Вспомогательные средства
Для облегчения работы можно воспользоваться имеющимся в проекте Makefile 
(на Windows для работы надо установить утилиту `make`).
Параметры:
- `style` - проверка кода на соответствие стилю
- `migrate` - выполнение миграций (создание и применений)
- `superuser` - создание суперпользователя
- `run` - запуск сервера в отладочном режиме

## Деплой

...

