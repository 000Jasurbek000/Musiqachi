import os
import django
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'education_portal.settings')
django.setup()

from main.models import Course, News, Resource

# Eski ma'lumotlarni o'chirish
Course.objects.all().delete()
News.objects.all().delete()
Resource.objects.all().delete()

print("Eski ma'lumotlar o'chirildi.")

# ========== KURSLAR ==========
courses_data = [
    {
        'title': 'Веб-разработка для начинающих',
        'category': 'ИТ Технологии',
        'short_description': 'Научитесь создавать современные веб-сайты с нуля. HTML, CSS, JavaScript и адаптивный дизайн.',
        'full_description': 'Полный курс веб-разработки, охватывающий основы HTML, CSS и JavaScript. Вы научитесь создавать адаптивные веб-сайты, работать с макетами и добавлять интерактивность. Курс адаптирован для людей с особыми потребностями.',
        'duration_text': '3 месяца',
        'level': 'Начальный',
        'students_count': 120,
        'lessons_count': 48,
        'price_text': 'Бесплатно',
        'author': 'Тимур Хасанов',
        'publication_year': 2024,
        'source_name': 'Образовательный центр',
        'source_url': '',
        'image_url': 'https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=800',
    },
    {
        'title': 'Английский язык A1-A2',
        'category': 'Языковые курсы',
        'short_description': 'Базовый курс английского языка с аудиоматериалами и интерактивными упражнениями.',
        'full_description': 'Комплексный курс английского языка для начинающих. Включает аудиоуроки, видеоматериалы с субтитрами и практические упражнения. Особое внимание уделяется произношению и восприятию речи на слух.',
        'duration_text': '6 месяцев и более',
        'level': 'Начальный',
        'students_count': 85,
        'lessons_count': 72,
        'price_text': 'Бесплатно',
        'author': 'Дилноза Юсупова',
        'publication_year': 2024,
        'source_name': 'Образовательный центр',
        'source_url': '',
        'image_url': 'https://images.unsplash.com/photo-1546410531-bb4caa6b424d?w=800',
    },
    {
        'title': 'Графический дизайн в Adobe Photoshop',
        'category': 'Творческие специальности',
        'short_description': 'Освойте профессию графического дизайнера. Работа с изображениями, создание баннеров и визиток.',
        'full_description': 'Практический курс по графическому дизайну с использованием Adobe Photoshop. Изучите инструменты редактирования, работу со слоями, цветокоррекцию и создание профессиональных макетов. Курс включает видеоуроки с подробными объяснениями.',
        'duration_text': '1 месяц',
        'level': 'Средний',
        'students_count': 64,
        'lessons_count': 36,
        'price_text': 'Бесплатно',
        'author': 'Алишер Камалов',
        'publication_year': 2024,
        'source_name': 'Образовательный центр',
        'source_url': '',
        'image_url': 'https://images.unsplash.com/photo-1626785774573-4b799315345d?w=800',
    }
]

for data in courses_data:
    Course.objects.create(**data)

print(f"✅ {len(courses_data)} ta kurs qo'shildi")

# ========== YANGILIKLAR ==========
news_data = [
    {
        'title': 'Новый набор на IT-курсы открыт!',
        'category': 'Объявления',
        'short_description': 'Приглашаем на обучение по направлениям веб-разработка, программирование и дизайн.',
        'content': '''Дорогие друзья! Мы рады сообщить об открытии нового набора на наши IT-курсы.

В этом наборе доступны следующие направления:
- Веб-разработка (HTML, CSS, JavaScript)
- Python программирование
- Графический дизайн в Adobe Photoshop

Все материалы адаптированы для людей с особыми потребностями. Обучение проводится в очном и дистанционном формате.

Запись открыта до конца месяца. Количество мест ограничено!''',
        'image_url': 'https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800',
        'published_at': datetime.now() - timedelta(days=2),
        'author': 'Администрация',
        'source_name': 'Образовательный центр',
        'source_url': '',
        'read_time': '2 мин чтения',
        'tags_text': 'IT курсы, Набор, Обучение',
    },
    {
        'title': 'Наши выпускники успешно трудоустроены',
        'category': 'Достижения',
        'short_description': 'Более 95% выпускников последнего потока нашли работу в течение 3 месяцев после окончания курсов.',
        'content': '''Мы гордимся успехами наших студентов!

В этом году выпустились 45 человек по различным направлениям. 43 из них уже работают в IT-компаниях, государственных учреждениях и частных организациях.

Особенно хочется отметить:
- Азиза А. - веб-разработчик в крупной IT-компании
- Тимур Б. - графический дизайнер в рекламном агентстве
- Малика С. - специалист технической поддержки

Мы продолжаем помогать нашим выпускникам в карьерном развитии и поддерживаем связь с работодателями.''',
        'image_url': 'https://images.unsplash.com/photo-1523240795612-9a054b0db644?w=800',
        'published_at': datetime.now() - timedelta(days=7),
        'author': 'Нигора Рахимова',
        'source_name': 'Образовательный центр',
        'source_url': '',
        'read_time': '3 мин чтения',
        'tags_text': 'Выпускники, Трудоустройство, Успех',
    },
    {
        'title': 'Открытие новой аудитории с современным оборудованием',
        'category': 'Мероприятия',
        'short_description': 'В нашем центре появилась новая учебная аудитория, оснащенная специализированным оборудованием.',
        'content': '''Отличная новость для наших студентов!

На прошлой неделе была открыта новая учебная аудитория, оборудованная:
- 15 современных компьютеров с большими экранами
- Специальное программное обеспечение для слабовидящих
- Система звукоусиления для аудиолекций
- Интерактивная доска с поддержкой жестов

Аудитория создана специально для комфортного обучения людей с ограниченными возможностями. 

Первые занятия в новой аудитории уже прошли, и студенты отметили высокое качество оборудования!''',
        'image_url': 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=800',
        'published_at': datetime.now() - timedelta(days=14),
        'author': 'Алишер Камалов',
        'source_name': 'Образовательный центр',
        'source_url': '',
        'read_time': '2 мин чтения',
        'tags_text': 'Оборудование, Аудитория, Новости',
    }
]

for data in news_data:
    News.objects.create(**data)

print(f"✅ {len(news_data)} ta yangilik qo'shildi")

# ========== MATERIALLAR ==========

# PDF Materiallar
pdf_data = [
    {
        'title': 'Введение в программирование на Python',
        'description': 'Полное руководство по основам программирования на Python. Включает примеры кода и практические задания.',
        'resource_type': 'pdf',
        'author': 'Иван Петров',
        'source_name': 'Python.org',
        'source_url': 'https://python.org',
        'year': 2023,
        'pages_count': 245,
        'file_size': '4.2 МБ',
        'thumbnail_url': 'https://images.unsplash.com/photo-1526379095098-d400fd0bf935?w=400',
        'external_url': '#',
    },
    {
        'title': 'HTML и CSS: Создание веб-страниц',
        'description': 'Учебник по веб-разработке для начинающих. Пошаговое руководство с иллюстрациями.',
        'resource_type': 'pdf',
        'author': 'Мария Сидорова',
        'source_name': 'WebDev Academy',
        'source_url': '',
        'year': 2024,
        'pages_count': 186,
        'file_size': '3.8 МБ',
        'thumbnail_url': 'https://images.unsplash.com/photo-1542831371-29b0f74f9713?w=400',
        'external_url': '#',
    },
    {
        'title': 'Английский язык для IT специалистов',
        'description': 'Специализированный учебник английского языка с IT терминологией и примерами из практики.',
        'resource_type': 'pdf',
        'author': 'Елена Волкова',
        'source_name': 'English IT',
        'source_url': '',
        'year': 2023,
        'pages_count': 312,
        'file_size': '5.6 МБ',
        'thumbnail_url': 'https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?w=400',
        'external_url': '#',
    }
]

# Audio Materiallar
audio_data = [
    {
        'title': 'Лекция: Основы веб-дизайна',
        'description': 'Аудиолекция о принципах современного веб-дизайна, композиции и цветовой теории.',
        'resource_type': 'audio',
        'author': 'Алексей Смирнов',
        'source_name': 'Design School',
        'source_url': '',
        'year': 2024,
        'duration_text': '45 мин',
        'file_size': '62 МБ',
        'thumbnail_url': 'https://images.unsplash.com/photo-1611162617213-7d7a39e9b1d7?w=400',
        'external_url': '#',
    },
    {
        'title': 'Английский язык: Разговорная практика',
        'description': 'Аудиокурс для развития навыков разговорного английского языка. Диалоги и упражнения.',
        'resource_type': 'audio',
        'author': 'John Smith',
        'source_name': 'English Audio',
        'source_url': '',
        'year': 2024,
        'duration_text': '1 ч 20 мин',
        'file_size': '85 МБ',
        'thumbnail_url': 'https://images.unsplash.com/photo-1590602847861-f357a9332bbc?w=400',
        'external_url': '#',
    },
    {
        'title': 'Введение в базы данных',
        'description': 'Аудиолекция о реляционных базах данных, SQL и проектировании структуры данных.',
        'resource_type': 'audio',
        'author': 'Сергей Николаев',
        'source_name': 'Database Academy',
        'source_url': '',
        'year': 2023,
        'duration_text': '55 мин',
        'file_size': '72 МБ',
        'thumbnail_url': 'https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=400',
        'external_url': '#',
    }
]

# Video Materiallar
video_data = [
    {
        'title': 'JavaScript для начинающих',
        'description': 'Видеокурс по основам JavaScript с примерами и практическими заданиями. Субтитры на русском языке.',
        'resource_type': 'video',
        'author': 'Дмитрий Кузнецов',
        'source_name': 'YouTube Education',
        'source_url': 'https://youtube.com',
        'year': 2024,
        'duration_text': '2 ч 15 мин',
        'quality_text': 'HD 1080p',
        'file_size': '850 МБ',
        'thumbnail_url': 'https://images.unsplash.com/photo-1579468118864-1b9ea3c0db4a?w=400',
        'external_url': 'https://youtube.com',
        'embed_url': 'https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ',
    },
    {
        'title': 'Photoshop: Обработка фотографий',
        'description': 'Видеоурок по профессиональной обработке фотографий в Adobe Photoshop. С жестовым переводом.',
        'resource_type': 'video',
        'author': 'Анна Павлова',
        'source_name': 'Design Channel',
        'source_url': '',
        'year': 2024,
        'duration_text': '1 ч 45 мин',
        'quality_text': 'HD 1080p',
        'file_size': '720 МБ',
        'thumbnail_url': 'https://images.unsplash.com/photo-1572044162444-ad60f128bdea?w=400',
        'external_url': 'https://youtube.com',
        'embed_url': 'https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ',
    },
    {
        'title': 'Git и GitHub для разработчиков',
        'description': 'Полное руководство по системе контроля версий Git и платформе GitHub. Для начинающих разработчиков.',
        'resource_type': 'video',
        'author': 'Максим Орлов',
        'source_name': 'Code Academy',
        'source_url': '',
        'year': 2024,
        'duration_text': '1 ч 30 мин',
        'quality_text': 'HD 720p',
        'file_size': '580 МБ',
        'thumbnail_url': 'https://images.unsplash.com/photo-1618401479427-c8ef9465fbe1?w=400',
        'external_url': 'https://youtube.com',
        'embed_url': 'https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ',
    }
]

# PDF qo'shish
for data in pdf_data:
    Resource.objects.create(**data)

print(f"✅ {len(pdf_data)} ta PDF material qo'shildi")

# Audio qo'shish
for data in audio_data:
    Resource.objects.create(**data)

print(f"✅ {len(audio_data)} ta Audio material qo'shildi")

# Video qo'shish
for data in video_data:
    Resource.objects.create(**data)

print(f"✅ {len(video_data)} ta Video material qo'shildi")

print("\n🎉 Barcha test ma'lumotlar muvaffaqiyatli qo'shildi!")
print(f"📚 Jami: {Course.objects.count()} kurs")
print(f"📰 Jami: {News.objects.count()} yangilik")
print(f"📄 Jami: {Resource.objects.filter(resource_type='pdf').count()} PDF")
print(f"🎧 Jami: {Resource.objects.filter(resource_type='audio').count()} Audio")
print(f"🎬 Jami: {Resource.objects.filter(resource_type='video').count()} Video")
