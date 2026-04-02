# Образовательный портал для слепых и глухих

Django проект с красивым дизайном в стиле my.gov.uz

## Установка

1. Создайте виртуальное окружение:
```bash
python -m venv venv
```

2. Активируйте виртуальное окружение:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Примените миграции:
```bash
python manage.py migrate
```

5. Создайте суперпользователя (для админ панели):
```bash
python manage.py createsuperuser
```

6. Запустите сервер:

```bash
python manage.py runserver
```

7. Откройте в браузере:
```
http://127.0.0.1:8000/
```

## Структура проекта

- `templates/` - HTML шаблоны
  - `base.html` - Базовый шаблон с header и footer
  - `home.html` - Главная страница
  - `courses.html` - Страница курсов
  - `news.html` - Новости
  - `contact.html` - Контакты
  - `about.html` - О нас

- `static/` - Статические файлы
  - `css/style.css` - Стили (цветовая схема my.gov.uz)
  - `js/voice.js` - Озвучивание для незрячих

- `main/` - Основное приложение
  - `views.py` - Представления
  - `urls.py` - URL маршруты
  - `models.py` - Модели данных

## Функции

✅ Header с логотипом и навигацией
✅ Footer с контактами
✅ 5 страниц: Главная, Курсы, Новости, Контакты, О нас
✅ Цветовая схема my.gov.uz
✅ Озвучивание для незрячих (Web Speech API)
✅ Адаптивный дизайн

## Цветовая схема

Все цвета вынесены в CSS переменные в `:root`:
- `--primary-blue: #1976D2`
- `--secondary-cyan: #00BCD4`
- `--accent-green: #4CAF50`
- И другие...

Чтобы изменить цвета - просто отредактируйте переменные в `static/css/style.css`
