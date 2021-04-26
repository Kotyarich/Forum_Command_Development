# TaskAggregator

Агрегатор задач сервисов GitHub, GitLab и Jira.

## Установка

Клонирование репозитория:
```bash
git clone https://github.com/Kotyarich/TaskAggregator_Team_Development.git
```

Создание виртуального окружения и установка пакетов:
```bash
cd TaskAggregator_Team_Development/task_aggregator
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Создание пользователя и базы данных PostgreSQL:
```bash
sudo su postgres
create user aggregator with password 'aggregator';
create database aggregator owner aggregator;
```

Выполнение миграций:
```bash
./manage.py makemigrations task_aggregator
./manage.py migrate
```

## Запуск

Запуск приложения на http://127.0.0.1:8000/:
```bash
./manage.py runserver
```

Запуск тестов:
```bash
./manage.py test
```
