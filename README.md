# CRM SYSTEM

***

### Описание приложения

#### CRM-система в виде веб-приложения для управления клиентами

#### Основные функции приложения:
- авторизация пользователя;
- создание, редактирование и просмотр предоставляемых услуг;
- создание, редактирование и просмотр рекламной кампании;
- создание, редактирование и просмотр потенциальных клиентов;
- создание, редактирование и просмотр контракта для клиента;
- перевод потенциального клиента в активного;
- подсчёт и отображение статистики по рекламным кампаниям: сколько привлечено потенциальных клиентов, сколько из них перешло в активных.

#### В системе есть преднастроенные роли пользователей.
- Администратор может создавать, просматривать и редактировать пользователей, назначать им роли и разрешения. Такой функционал реализует административная панель Django.
- Оператор может создавать, просматривать и редактировать потенциальных клиентов.
- Маркетолог может создавать, просматривать и редактировать предоставляемые услуги и рекламные кампании.
- Менеджер может создавать, просматривать и редактировать контракты, смотреть потенциальных клиентов и переводить их в активных.
- Все роли могут смотреть статистику рекламных кампаний.

***

## Запуск проекта

***

### Важно

У вас должен быть установлен docker

***

### Создать виртуальное окружение

```python3 -m venv venv```

```source venv/bin/activate``` - для линукс

### Установить зависимости

```pip install -r requirements.txt```

### Перейтти в папку с проектом

```cd crm_project```

### Создать переменные окружения

Создать файл .env с переменными окружения по аналогии как в 
файле .env.template

### Запустить сборку проекта

```docker compose up -d```

### Создать администратора

```docker compose exec -ti crm python3 manage.py createsuperuser```

### Создать заранее настроенные группы

```docker compose exec -ti crm python3 manage.py loaddata fixture/group-fixture.json```

### Приложение готово к использованию

Перейдите по адресу http://127.0.0.1:8000/ если тестируете локально.