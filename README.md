# MemontDiary

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/doc/)
[![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)](https://www.jetbrains.com/pycharm/documentation/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white&color=092E20&labelColor=gray)](https://www.djangoproject.com/start/)
[![HTML](https://img.shields.io/badge/HTML-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS](https://img.shields.io/badge/CSS-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)](https://docs.github.com/en/actions)
[![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/docs/)
[![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)](https://redis.readthedocs.io/en/latest/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white&color=2496ED&labelColor=gray)](https://docs.docker.com/)

## Web application of personal diary

### Описание
Проект реализует бэкенд и фронтенд веб-приложения для ведения личного дневника.  
Inspired by https://dayone.me

### Функционал:

1. **Регистрация и аутентификация пользователей:** 
   - Пользователи могут зарегистрироваться, войти в систему и выйти из неё.
   - Регистрация и аутентификация реализованы через email пользователя.
   - Осуществлены верификация с помощью кода, который отправляется приложением на почту, и возможность сброса пароля.
2. **Создание, редактирование и удаление записей в дневнике:** 
   - Авторизованные пользователи могут добавлять новые записи в дневник, редактировать существующие записи (только свои) и удалять ненужные записи.
   - Есть возможность добавлять изображение для записи.
   - При создании записи автоматически сохраняется дата и время.
   - Все записи имеют флаг публичности. Публичные записи могут появляться на главной странице в открытом доступе.
3. **Просмотр записей:** 
   - Пользователи могут просматривать список всех своих записей.
   - Пользователи могут просматривать отдельные записи в подробном виде.
   - Пользователи могут просматривать некоторые случайные публичные записи других пользователей на главной странице.
4. **Поиск по записям:** 
   - Пользователи могут искать записи по заголовку или содержимому через поиск навигационной панели.
5. **Кэш:** 
   - В приложении дневника реализовано кеширование детального просмотра записей.

### Требования
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Запуск
1. Клонируйте репозиторий с помощью команды и перейдите в папку проекта:
```shell
git clone https://github.com/ialar/MemontDiary.git
cd MemontDiary
```
2. Создайте файл .env на основе .env.sample и заполните его своими данными:
```bash
cp .env.example .env
```
3. Соберите образы и запустите контейнеры командой:
```bash
docker-compose up -d --build
```

### Создание суперпользователя
Чтобы создать суперпользователя, выполните команду:
```bash
docker-compose exec <container_name_or_id> python manage.py csu
```

### Наполнение БД
При необходимости наполните базу данных с помощью фикстур:
```bash
docker-compose exec memont_diary python manage.py loaddata fixtures/users.json
docker-compose exec memont_diary python manage.py loaddata fixtures/diary.json
```

### Доступ и работа с приложением
- Главная: http://localhost:8000/
- Админка: http://localhost:8000/admin/