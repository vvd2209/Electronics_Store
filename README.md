# Онлайн платформа торговой сети электроники
Это веб-приложение представляет собой онлайн-платформу для торговой сети электроники. Приложение позволяет управлять иерархической структурой сети по продаже электроники, включая заводы, розничные сети и индивидуальных предпринимателей. Вы можете создавать, редактировать и удалять объекты сети, а также управлять продуктами, контактами и задолженностью перед поставщиком.
### Возможности проекта
- CRUD пользователей.
- CRUD продуктов.
- CRUD торговых сетей.
- CRUD поставщиков.
- Отслеживание задолженности перед поставщиком.
- Админ-панель с возможностью добавления ссылки на "Поставщика", фильтрации по названию города и "admin action" для очистки задолженности перед поставщиком..
### Запуск проекта
1. Склонируйте репозиторий:
    - [github.com](https://github.com/vvd2209/Electronics_Store)
2. Установите и активируйте виртуальное окружение.
3. Установите зависимости:
    - pip install -r requirements.txt
4. Создайте файл .env в корневой директории и заполните необходимые переменные окружения по шаблону .env.sample.
5. Примените миграции:
    - python manage.py migrate
6. Запустите сервер:
     - python manage.py runserver
7. Используйте команду для создания суперпользователя для доступа в административную панель:
    - python manage.py createsuperuser
### Права доступа
Доступ к API имеют только активные сотрудники.
### Документация API
Документация API доступна после запуска сервера по ссылке **[redoc](http://127.0.0.1:8000/redoc/)**
