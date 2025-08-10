# Easylink

Минимальный прототип сервиса сокращения ссылок на Django.

## Возможности
- Создание коротких ссылок через REST API.
- Перенаправление по коротким ссылкам и запись кликов.
- Управление ссылками через Django admin.
- Swagger-документация по адресу `/swagger/`.
- Обращения в техподдержку через эндпоинт `/api/support/tickets/`.
- Управление группами ссылок, доменами и пикселями через REST API.
- Создание и использование API ключей для доступа к API (`/api/keys/`, заголовок `X-API-Key`).

## Запуск
```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
