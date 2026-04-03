from django.core.exceptions import ValidationError
from django.db import models


# ============================================
# KURS MODELLARI (Course Models)
# ============================================

class Course(models.Model):
    # Choices
    CATEGORY_CHOICES = [
        ('ИТ Технологии', 'ИТ Технологии'),
        ('Языковые курсы', 'Языковые курсы'),
        ('Реабилитация', 'Реабилитация'),
        ('Творческие специальности', 'Творческие специальности'),
        ('Профессиональное образование', 'Профессиональное образование'),
        ('Личностное развитие', 'Личностное развитие'),
        ('Здоровье и спорт', 'Здоровье и спорт'),
        ('Социальная адаптация', 'Социальная адаптация'),
        ('Другое', 'Другое'),
    ]
    
    LEVEL_CHOICES = [
        ('Начальный', 'Начальный'),
        ('Средний', 'Средний'),
        ('Продвинутый', 'Продвинутый'),
    ]
    
    DURATION_CHOICES = [
        ('1 неделя', '1 неделя'),
        ('15 дней', '15 дней'),
        ('1 месяц', '1 месяц'),
        ('3 месяца', '3 месяца'),
        ('6 месяцев и более', '6 месяцев и более'),
    ]
    
    title = models.CharField(
        max_length=255,
        verbose_name='Название курса',
        help_text='Полное название курса.'
    )
    category = models.CharField(
        max_length=120,
        choices=CATEGORY_CHOICES,
        verbose_name='Категория',
        help_text='Выберите категорию курса.'
    )
    short_description = models.TextField(
        verbose_name='Краткое описание',
        help_text='Краткое описание для карточки курса.'
    )
    full_description = models.TextField(
        verbose_name='Полное описание',
        help_text='Полное описание для детальной страницы курса.'
    )
    duration_text = models.CharField(
        max_length=120,
        choices=DURATION_CHOICES,
        verbose_name='Текст длительности',
        help_text='Выберите продолжительность курса.'
    )
    level = models.CharField(
        max_length=120,
        choices=LEVEL_CHOICES,
        verbose_name='Уровень',
        help_text='Выберите уровень сложности.'
    )
    students_count = models.PositiveIntegerField(
        verbose_name='Количество студентов',
        help_text='Сколько студентов обучается.'
    )
    lessons_count = models.PositiveIntegerField(
        verbose_name='Количество уроков',
        help_text='Общее количество уроков в курсе.'
    )
    price_text = models.CharField(
        max_length=120,
        verbose_name='Текст цены',
        help_text='Например: Бесплатно.',
        default='Бесплатно'
    )
    author = models.CharField(
        max_length=255,
        verbose_name='Автор/преподаватель',
        help_text='Имя автора курса.'
    )
    publication_year = models.PositiveIntegerField(
        verbose_name='Год публикации',
        help_text='Год публикации материала.'
    )
    source_name = models.CharField(
        max_length=255,
        verbose_name='Источник',
        help_text='Название источника или организации.'
    )
    source_url = models.CharField(
        max_length=255,
        verbose_name='Ссылка на источник',
        help_text='Ссылка на источник.',
        blank=True
    )
    image_url = models.URLField(
        verbose_name='Ссылка на изображение',
        help_text='Ссылка на изображение карточки.',
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to='courses/',
        verbose_name='Изображение курса',
        help_text='Загрузите изображение с компьютера.',
        blank=True,
        null=True
    )
    pdf_file = models.FileField(
        upload_to='courses/pdfs/',
        verbose_name='PDF-файл курса',
        help_text='Файл PDF для чтения.',
        blank=True,
        null=True
    )
    audio_file = models.FileField(
        upload_to='courses/audio/',
        verbose_name='Аудиофайл курса',
        help_text='Аудиоверсия материала.',
        blank=True,
        null=True
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликован',
        help_text='Показывать ли курс на сайте.'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    @property
    def pdf_url(self):
        return self.pdf_file.url if self.pdf_file else ''

    @property
    def audio_url(self):
        return self.audio_file.url if self.audio_file else ''


# ============================================
# YANGILIK MODELLARI (News Models)
# ============================================

class News(models.Model):
    # Choices
    CATEGORY_CHOICES = [
        ('Международные новости', 'Международные новости'),
        ('Мероприятия', 'Мероприятия'),
        ('Образование', 'Образование'),
        ('Технологии', 'Технологии'),
        ('Достижения', 'Достижения'),
        ('Партнерство', 'Партнерство'),
        ('Объявления', 'Объявления'),
        ('Другое', 'Другое'),
    ]
    
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок новости',
        help_text='Полный заголовок новости.'
    )
    category = models.CharField(
        max_length=120,
        choices=CATEGORY_CHOICES,
        verbose_name='Категория',
        help_text='Выберите категорию новости.'
    )
    short_description = models.TextField(
        verbose_name='Краткое описание',
        help_text='Краткое описание для карточки.'
    )
    content = models.TextField(
        verbose_name='Полный текст новости',
        help_text='Полный текст новости.'
    )
    image_url = models.URLField(
        verbose_name='Ссылка на изображение',
        help_text='Ссылка на главное изображение.',
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to='news/',
        verbose_name='Изображение новости',
        help_text='Загрузите изображение с компьютера.',
        blank=True,
        null=True
    )
    published_at = models.DateTimeField(
        verbose_name='Дата публикации',
        help_text='Дата и время публикации.'
    )
    author = models.CharField(
        max_length=255,
        verbose_name='Автор',
        help_text='Автор новости.'
    )
    source_name = models.CharField(
        max_length=255,
        verbose_name='Источник',
        help_text='Источник публикации.'
    )
    source_url = models.CharField(
        max_length=255,
        verbose_name='Ссылка на источник',
        help_text='Ссылка на внешний источник.',
        blank=True
    )
    read_time = models.CharField(
        max_length=120,
        verbose_name='Время чтения',
        help_text='Например: 5 мин чтения.'
    )
    views_count = models.PositiveIntegerField(
        verbose_name='Количество просмотров',
        default=0
    )
    likes_count = models.PositiveIntegerField(
        verbose_name='Количество лайков',
        default=0
    )
    tags_text = models.CharField(
        max_length=255,
        verbose_name='Теги',
        help_text='Перечислите теги через запятую.',
        blank=True
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликована',
        help_text='Показывать ли новость на сайте.'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-published_at', '-created_at']

    def __str__(self):
        return self.title

    @property
    def tags_list(self):
        if not self.tags_text:
            return []
        return [tag.strip() for tag in self.tags_text.split(',') if tag.strip()]

    @property
    def content_paragraphs(self):
        return [p.strip() for p in self.content.split('\n') if p.strip()]


# ============================================
# MATERIAL MODELLARI (Resource Models)
# ============================================

class Resource(models.Model):
    RESOURCE_TYPES = [
        ('pdf', 'PDF документ'),
        ('audio', 'Аудио'),
        ('video', 'Видео')
    ]

    title = models.CharField(
        max_length=255,
        verbose_name='Название материала',
        help_text='Название материала.'
    )
    description = models.TextField(
        verbose_name='Описание материала',
        help_text='Краткое описание.'
    )
    resource_type = models.CharField(
        max_length=10,
        choices=RESOURCE_TYPES,
        verbose_name='Тип материала',
        help_text='Выберите тип: PDF, аудио или видео.'
    )
    author = models.CharField(
        max_length=255,
        verbose_name='Автор',
        help_text='Автор или лектор.'
    )
    source_name = models.CharField(
        max_length=255,
        verbose_name='Источник',
        help_text='Источник или организация.'
    )
    source_url = models.CharField(
        max_length=255,
        verbose_name='Ссылка на источник',
        blank=True
    )
    year = models.PositiveIntegerField(
        verbose_name='Год',
        help_text='Год публикации.'
    )
    pages_count = models.PositiveIntegerField(
        verbose_name='Количество страниц',
        help_text='Для PDF-материалов.',
        blank=True,
        null=True
    )
    duration_text = models.CharField(
        max_length=120,
        verbose_name='Длительность',
        help_text='Для аудио и видео. Например: 45 мин.',
        blank=True
    )
    file_size = models.CharField(
        max_length=120,
        verbose_name='Размер файла',
        help_text='Например: 4.2 МБ.'
    )
    quality_text = models.CharField(
        max_length=120,
        verbose_name='Качество видео',
        help_text='Только для видео. Например: HD 1080p.',
        blank=True
    )
    thumbnail_url = models.URLField(
        verbose_name='Ссылка на изображение',
        help_text='Ссылка на обложку.',
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to='resources/images/',
        verbose_name='Изображение материала',
        help_text='Загрузите изображение с компьютера.',
        blank=True,
        null=True
    )
    file = models.FileField(
        upload_to='resources/files/',
        verbose_name='Файл материала',
        help_text='Загрузите PDF или аудиофайл.',
        blank=True,
        null=True
    )
    external_url = models.CharField(
        max_length=255,
        verbose_name='Внешняя ссылка',
        help_text='Ссылка на скачивание или YouTube.',
        blank=True
    )
    embed_url = models.CharField(
        max_length=255,
        verbose_name='Ссылка для встраивания',
        help_text='Только для видео.',
        blank=True
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликован',
        help_text='Показывать ли материал на сайте.'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Учебный материал'
        verbose_name_plural = 'Учебные материалы'
        ordering = ['resource_type', 'title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Fayl hajmini avtomatik aniqlash
        if self.file and not self.file_size:
            size_bytes = self.file.size
            if size_bytes < 1024:
                self.file_size = f'{size_bytes} Б'
            elif size_bytes < 1024 * 1024:
                size_kb = size_bytes / 1024
                self.file_size = f'{size_kb:.1f} КБ'
            elif size_bytes < 1024 * 1024 * 1024:
                size_mb = size_bytes / (1024 * 1024)
                self.file_size = f'{size_mb:.1f} МБ'
            else:
                size_gb = size_bytes / (1024 * 1024 * 1024)
                self.file_size = f'{size_gb:.2f} ГБ'
        super().save(*args, **kwargs)

    def clean(self):
        errors = {}
        if self.resource_type == 'pdf':
            if not self.pages_count:
                errors['pages_count'] = 'Для PDF укажите количество страниц.'
            if not self.file and not self.external_url:
                errors['file'] = 'Для PDF загрузите файл или укажите ссылку.'
        if self.resource_type == 'audio':
            if not self.duration_text:
                errors['duration_text'] = 'Для аудио укажите длительность.'
            if not self.file and not self.external_url:
                errors['file'] = 'Для аудио загрузите файл или укажите ссылку.'
        if self.resource_type == 'video':
            if not self.duration_text:
                errors['duration_text'] = 'Для видео укажите длительность.'
            if not self.quality_text:
                errors['quality_text'] = 'Для видео укажите качество.'
            if not self.embed_url:
                errors['embed_url'] = 'Для видео укажите ссылку для встраивания.'
            if not self.external_url:
                errors['external_url'] = 'Для видео укажите внешнюю ссылку.'
        if errors:
            raise ValidationError(errors)

    @property
    def file_url(self):
        if self.file:
            return self.file.url
        return self.external_url


# ============================================
# ОСНОВАТЕЛЬ (Founder)
# ============================================

class Founder(models.Model):
    full_name = models.CharField(
        max_length=255,
        verbose_name='ФИО',
        help_text='Полное имя основателя'
    )
    position = models.CharField(
        max_length=255,
        verbose_name='Должность',
        help_text='Должность основателя (например: Директор издательства)'
    )
    company = models.CharField(
        max_length=255,
        verbose_name='Организация',
        blank=True,
        help_text='Название организации'
    )
    photo = models.ImageField(
        upload_to='founder/',
        verbose_name='Фотография',
        blank=True,
        null=True,
        help_text='Фото основателя'
    )
    bio = models.TextField(
        verbose_name='Краткая биография',
        blank=True,
        help_text='Краткая информация об основателе'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Отображать на сайте',
        help_text='Показывать блок основателя на странице "О нас"'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        verbose_name = 'Основатель'
        verbose_name_plural = 'Основатели'
        ordering = ['-created_at']

    def __str__(self):
        return self.full_name
