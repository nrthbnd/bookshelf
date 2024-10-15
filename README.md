# Приложение для управления списком книг bookshelf

### Используемые технологии
- FastAPI – для создания веб-API;
- PostgreSQL – для хранения данных;
- gRPC – для межсервисного взаимодействия;
- RabbitMQ – брокер сообщений для взаимодействия между сервисами;
- Alembic – для управления миграциями базы данных;
- JWT – для аутентификации пользователей;
- Docker – для контейнеризации сервисов;
- Poetry – для управления зависимостями.

### Как запустить bookshelf:
1. Клонировать репозиторий и перейти в него в командной строке:
`git clone https://github.com/nrthbnd/bookshelf.git`
2. Cоздать и активировать виртуальное окружение:
`python -m venv .venv`
`source venv/scripts/activate`
или
`source venv/bin/activate`
3. Установить зависимости с помощью poetry:
`poetry install`
4. Заполнить файлы с переменными окружения `.env` и `.env.rmq`
в соответствии с примерами `.env.example` и `.env.rmq.example`.
5. Соберать и запустить контейнеры с помощью Docker Compose:
`docker-compose up --build`
Будут запущены контейнеры fastapi, grpc, db, rabbitmq и consumer.

### Использование проекта
Документация Swagger для web-api будет доступна:
- `http://localhost:8000/docs`

Для использования GRPC-сервиса в Postman: выбрать request type GRPC,
импоровать файл `app/grpc_service/proto/book.proto`, перейти на `localhost:50051`,
и выбрать необходимый метод:
- ListBooks для получения списка всех доступных книг;
- GetBookById для получения книги по id, при этом необходимо указать 
message `{"id": 1}`.

При использовании небезопасных методов в fastapi (post, update, delete запросы к книгам)
с помощью RabbitMQ записывается лог о пришедшем сообщении и выводится в консоль. 

