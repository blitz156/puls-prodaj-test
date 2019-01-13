**Для запуска должны быть установлены:**

1. `docker` [https://docs.docker.com/install/linux/docker-ce/ubuntu/]
2. `docker-compose` [https://docs.docker.com/compose/install/]
3. `apt-get install fabric`

**Запуск локально:**

1. ``docker-compose up``

**Запуск в продакшене:**

1. ``docker-compose --file docker-compose.production.yml up -d``


**P.S.**

Запущеное и рабочее приложение можно проверить по адресу:
 - http://5.189.228.198/v1/skills
 - http://5.189.228.198/v1/skills/UUID
 
Вообще говоря результат ответа отличается от ответов прокси серверов,
чтобы была наглядность откуда взялись данные (либо из кеша, либо от прокси серверов)