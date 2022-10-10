![Yamdb Workflow Status](https://github.com/wegnagun/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?branch=master&event=push)

# api_yamdb
api_yamdb
Проект **YaMDb** собирает **отзывы (Review)** пользователей на **произведения (Titles)**. Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список **категорий (Category)** может быть расширен администратором (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).
Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

В каждой категории есть произведения: книги, фильмы или музыка. Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Насекомые» и вторая сюита Баха.
Произведению может быть присвоен жанр (Genre) из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). Новые жанры может создавать только администратор.
 
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы (Review) и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.

## Автор  
[Александр Фокин](https://github.com/Wegnagun)

## Технологии
Python 3.7, Django 2.2, DRF, JWT, NGINX, PostgreSQL, Docker, Docker-compose

### Установка: 
#### Windows
`python -m venv venv `

`venv/Scripts/activate `

`python -m pip install --upgrade pip `

перейти в дирректорию api_yamdb  

`pip install -r requirements.txt `

#### Linux
`python3 -m venv venv `

`source venv/bin/activate `

`python -m pip install --upgrade pip `

`pip install --upgrade setuptools ` опционально...

`python -m pip install --upgrade pip setuptools` либо так)  

перейти в дирректорию api_yamdb  

`pip install -r requirements.txt `

### Запуск
создайте файл .env в дирректории **infra** и добавьте значения необходимым константам по шаблону:  
`DB_ENGINE=django.db.backends.postgresql`  
`DB_NAME=postgres`  
`POSTGRES_USER=postgres`  
`POSTGRES_PASSWORD=postgres`  
`DB_HOST=db`  
`DB_PORT=5432`  
`KEY='your django secret key`  

Перейдити в дирректорию **api_yamdb** и выполните миграции:

`python manage.py migrate `

Запустите сервер:

`python manage.py runserver`  

### Работа с Docker  

перейти в дирректорию с Dockerfile  
`docker build -t Имя_проекта .` создание докер образа  
перейти в дирректорию с docker-compose.yaml  
`docker-compose up -d` создание комплекса докер контейнеров  

выполните команды после запуска контейнера:  
`docker-compose exec имя_веб_контейнера python manage.py migrate`  
`docker-compose exec имя_веб_контейнера python manage.py createsuperuser`  
`docker-compose exec имя_веб_контейнера python manage.py collectstatic --no-input`  

либо подгрузить образец заполненной базы данных:  
`docker cp fixtures.json имя_веб_контейнера:/app/ ` копируем фикстуру в контейнер  
`python manage.py loaddata fixtures.json` наполняем базу  

### Пользовательские роли
- **Аноним** — может просматривать описания произведений, читать отзывы и комментарии.
- **Аутентифицированный пользователь (user)** — может, как и Аноним, читать всё, дополнительно он может публиковать отзывы и ставить оценку произведениям (фильмам/книгам/песенкам), может комментировать чужие отзывы; может редактировать и удалять свои отзывы и комментарии. Эта роль присваивается по умолчанию каждому новому пользователю.
- **Модератор (moderator)** — те же права, что и у Аутентифицированного пользователя плюс право удалять любые отзывы и комментарии.
- **Администратор (admin)** — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.
- **Суперюзер Django** — обладет правами администратора (admin)

### Регистрация нового пользователя
Получить код подтверждения на переданный email.
Права доступа: Доступно без токена.
Использовать имя 'me' в качестве username запрещено.
Поля email и username должны быть уникальными.

Регистрация нового пользователя:
```
POST /api/v1/auth/signup/

{
  "email": "string",
  "username": "string"
}
```

Получение JWT-токена:
```
POST /api/v1/auth/token/

{
  "username": "string",
  "confirmation_code": "string"
}
```

### Ресурсы API YaMDb
- Ресурс **auth**: аутентификация.
- Ресурс **users**: пользователи.
- Ресурс **comments**: комментарии к отзывам. Комментарий привязан к определённому отзыву.
- Ресурс **genres**: жанры произведений.
- Ресурс **categories**: категории произведений.
- Ресурс **titles**: произведения.
