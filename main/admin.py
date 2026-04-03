from django.contrib import admin
from .models import Course, News, Resource, Founder

admin.site.site_header = 'Образовательный портал - Панель управления'
admin.site.site_title = 'Админ панель'
admin.site.index_title = 'Добро пожаловать в панель управления'


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'level', 'duration_text', 'students_count', 'is_published', 'created_at')
    list_filter = ('is_published', 'category', 'level', 'publication_year')
    search_fields = ('title', 'author', 'category')
    list_editable = ('is_published',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Основные данные', {
            'fields': ('title', 'category', 'level', 'short_description', 'full_description')
        }),
        ('Длительность и статистика', {
            'fields': ('duration_text', 'students_count', 'lessons_count', 'price_text')
        }),
        ('Автор и источник', {
            'fields': ('author', 'publication_year', 'source_name', 'source_url')
        }),
        ('Медиа', {
            'fields': ('image_url', 'image', 'pdf_file', 'audio_file'),
            'description': 'Вы можете указать ссылку на изображение ИЛИ загрузить файл с компьютера'
        }),
        ('Публикация', {
            'fields': ('is_published', 'created_at', 'updated_at')
        }),
    )


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'published_at', 'author', 'views_count', 'is_published', 'created_at')
    list_filter = ('is_published', 'category', 'published_at')
    search_fields = ('title', 'author', 'category', 'tags_text')
    list_editable = ('is_published',)
    readonly_fields = ('views_count', 'likes_count', 'created_at', 'updated_at')
    date_hierarchy = 'published_at'
    fieldsets = (
        ('Основные данные', {
            'fields': ('title', 'category', 'short_description', 'content', 'published_at')
        }),
        ('Автор и источник', {
            'fields': ('author', 'source_name', 'source_url')
        }),
        ('Медиа и метаданные', {
            'fields': ('image_url', 'image', 'read_time', 'tags_text'),
            'description': 'Вы можете указать ссылку на изображение ИЛИ загрузить файл с компьютера'
        }),
        ('Статистика (автоматически)', {
            'fields': ('views_count', 'likes_count'),
            'description': 'Эти поля обновляются автоматически и не редактируются вручную'
        }),
        ('Публикация', {
            'fields': ('is_published', 'created_at', 'updated_at')
        }),
    )


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'resource_type', 'author', 'year', 'is_published', 'created_at')
    list_filter = ('is_published', 'resource_type', 'year')
    search_fields = ('title', 'author', 'description')
    list_editable = ('is_published',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Основные данные', {
            'fields': ('title', 'description', 'resource_type')
        }),
        ('Автор и источник', {
            'fields': ('author', 'source_name', 'source_url', 'year')
        }),
        ('Изображение', {
            'fields': ('thumbnail_url', 'image'),
            'description': 'Вы можете указать ссылку на изображение ИЛИ загрузить файл с компьютера'
        }),
        ('Файл и характеристики', {
            'fields': ('file', 'pages_count', 'duration_text', 'quality_text'),
            'description': 'PDF/Аудио: загрузите файл. Видео: укажите YouTube ссылки ниже. Pages - только для PDF, Duration - для аудио/видео, Quality - только для видео'
        }),
        ('Видео ссылки (только для YouTube)', {
            'fields': ('external_url', 'embed_url'),
            'description': 'External URL - обычная ссылка YouTube, Embed URL - для встраивания'
        }),
        ('Публикация', {
            'fields': ('is_published', 'created_at', 'updated_at')
        }),
    )


@admin.register(Founder)
class FounderAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'company', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('full_name', 'position', 'company')
    list_editable = ('is_active',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Основные данные', {
            'fields': ('full_name', 'position', 'company')
        }),
        ('Фото и биография', {
            'fields': ('photo', 'bio')
        }),
        ('Настройки отображения', {
            'fields': ('is_active', 'created_at', 'updated_at')
        }),
    )
