# CRM SYSTEM

***

## Запуск проекта

***

### Важно

У вас должен быть установлен docker

***

### Создать виртуальное окружение

```python3 -m venv venv```

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

### Приложение готово к использованию

Перейдите по адресу http://127.0.0.1:8000/ если тестируете локально.