# SPEEDSOLVER

# PUBLIC:
- https://speedsolver.ru/ - основной сайт.
- https://api.speedsolver.ru/docs - документация к API

## Описание

***SPEEDSOLVER*** — это **SaaS** система управления проектами, предназначенная для эффективного управления командами, проектами, задачами, подзадачами и дедлайнами. Проект помогает командам организовать свою работу, отслеживать прогресс и достигать поставленных целей в срок.

## Содержание

- [Описание](#описание)
- [Функции](#функции)
- [Стек технологий](#стек-технологий)
- [Установка](#установка)
- [Лицензия](#лицензия)

## Функции

- **Управление командами**: Создание и управление командами, добавление и удаление участников.
- **Управление проектами**: Создание и управление проектами, назначение задач и подзадач. Общение в реальном времени внутри проекта с сохранением истории чата.
- **Управление задачами**: Создание, редактирование и удаление задач, назначение ответственных лиц.
- **Управление подзадачами**: Создание, редактирование и удаление подзадач, отслеживание прогресса.
- **Дедлайны**: Установка и отслеживание дедлайнов для задач и подзадач.
- **Уведомления**: Автоматические уведомления о приближающихся дедлайнах и изменениях в задачах.

## Стек технологий

- **Frontend**: Vue.js
- **Backend**: Python - FastAPI, Python WebSockets
- **Mobile** Swift - Storyboard
- **Object Relational Mapping**: Python SQLAlchemy + Alembic
- **База данных**: PostgreSQL
- **Аутентификация & Авторизация**: JWT (JSON Web Tokens)
- **Дополнительно**:
   - Docker – контейнеризация/рзавертывание приложения.
   - Redis – Кэш-хранилище.
   - Nginx - Веб-сервер для проксирования внешних подключений путем **reverse proxy**, реализация защищенного соединения с **SSL/TLS**, проксирование поддоменов.
   - Github Actions (CI/CD) – непрерывная интеграции и непрерывной доставки.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/xxxw1tnessbtwxxx/SpeedSolver.git

2. Необходимо переназначить порты в файлах **SpeedSolverAPI/docker/docker-compose.yml, SpeedSolverFrontend/docker-compose.web.yml, WebSocket/Dockerfile** в случае, если у вас заняты:
   - API:HTTP - 5678
   - PostgreSQL - 5435
   - WebSocket Server - 8765
   - Redis Instance - 6379
4. Запустите Docker Engine на вашем компьютере или виртуальной машине.
5. Запустите контейнер Docker:
   ```bash
   cd SpeedSolver/SpeedSolverAPI 
   make run (при использовании macOS/Linux)
   docker-compose up --build -d (при использовании Windows)

Документация к API будет создана автоматически с помощью Swagger UI. Получить документацию можно по адресу: https://your-ip:your-port/swagger/index.html

## Лицензия
Данный программный продукт свободно распространяется под описаннымии правилами Apache License 2.0. Для ознакомления - [click](https://github.com/w1tnessbtwwwww/SpeedSolver/blob/master/LICENSE).