from django.shortcuts import get_object_or_404, render
from django.utils.formats import date_format
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Course, News, Resource


def serialize_course(course):
    # Rasmni aniqlash: birinchi image faylini, keyin image_url ni ishlatish
    image = course.image.url if course.image else course.image_url
    
    return {
        'id': course.id,
        'title': course.title,
        'category': course.category,
        'description': course.short_description,
        'duration': course.duration_text,
        'level': course.level,
        'students': course.students_count,
        'lessons': course.lessons_count,
        'price': course.price_text,
        'image': image,
    }


def serialize_news_item(item):
    # Rasmni aniqlash: birinchi image faylini, keyin image_url ni ishlatish
    image = item.image.url if item.image else item.image_url
    
    return {
        'id': item.id,
        'image': image,
        'date': date_format(item.published_at, 'j E Y'),
        'title': item.title,
        'description': item.short_description,
        'views_count': item.views_count,
        'likes_count': item.likes_count,
    }



def home(request):
    # Bosh sahifa statik bo'ladi
    return render(request, 'home.html')


def courses(request):
    courses_qs = Course.objects.filter(is_published=True)
    context = {
        'courses_data': [serialize_course(course) for course in courses_qs],
        'categories': Course.CATEGORY_CHOICES,
        'levels': Course.LEVEL_CHOICES,
        'durations': Course.DURATION_CHOICES,
    }
    return render(request, 'courses.html', context)


def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id, is_published=True)
    return render(request, 'course_detail.html', {'course': course})


def news(request):
    news_qs = News.objects.filter(is_published=True)
    context = {
        'news_data': [serialize_news_item(item) for item in news_qs],
    }
    return render(request, 'news.html', context)


def news_detail(request, news_id):
    article = get_object_or_404(News, pk=news_id, is_published=True)
    
    # Ko'rishlar sonini oshirish (faqat birinchi marta ko'rganda)
    viewed_news = request.session.get('viewed_news', [])
    if news_id not in viewed_news:
        article.views_count += 1
        article.save(update_fields=['views_count'])
        viewed_news.append(news_id)
        request.session['viewed_news'] = viewed_news
    
    related_news = News.objects.filter(is_published=True).exclude(pk=article.pk)[:3]
    
    # Foydalanuvchi layk qo'yganmi tekshirish
    liked_news = request.session.get('liked_news', [])
    user_has_liked = news_id in liked_news
    
    context = {
        'article': article,
        'related_news': related_news,
        'user_has_liked': user_has_liked,
    }
    return render(request, 'news_detail.html', context)


def resources(request):
    resources_qs = Resource.objects.filter(is_published=True)
    context = {
        'pdf_resources': resources_qs.filter(resource_type='pdf'),
        'audio_resources': resources_qs.filter(resource_type='audio'),
        'video_resources': resources_qs.filter(resource_type='video'),
    }
    return render(request, 'resources.html', context)


def contact(request):
    # Kontakt sahifa statik bo'ladi
    return render(request, 'contact.html')


@csrf_exempt
def contact_submit(request):
    if request.method == 'POST':
        try:
            from django.core.mail import send_mail
            from django.conf import settings
            
            data = json.loads(request.body)
            name = data.get('name', '')
            email = data.get('email', '')
            phone = data.get('phone', '')
            subject = data.get('subject', '')
            message = data.get('message', '')
            
            # Email matnini tayyorlash
            email_subject = f'Новое сообщение с сайта: {subject}'
            email_body = f"""
Новое сообщение от посетителя сайта:

Имя: {name}
Email: {email}
Телефон: {phone}
Тема: {subject}

Сообщение:
{message}

---
Отправлено с образовательного портала
            """
            
            # Email yuborish
            send_mail(
                subject=email_subject,
                message=email_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            
            return JsonResponse({
                'success': True,
                'message': 'Ваше сообщение успешно отправлено! Мы свяжемся с вами в ближайшее время.'
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'Ошибка при отправке сообщения: {str(e)}'
            })
    
    return JsonResponse({
        'success': False,
        'message': 'Неверный метод запроса'
    })


def about(request):
    from .models import Founder
    
    # Faol asoschi ma'lumotini olish
    founder = Founder.objects.filter(is_active=True).first()
    
    context = {
        'founder': founder
    }
    
    return render(request, 'about.html', context)


def search(request):
    query = request.GET.get('q', '').strip()
    
    context = {
        'query': query,
        'courses': [],
        'news': [],
        'resources': [],
        'total_results': 0,
    }
    
    if query:
        # Kurslardan qidirish
        courses = Course.objects.filter(
            Q(title__icontains=query) | 
            Q(short_description__icontains=query) | 
            Q(category__icontains=query),
            is_published=True
        )[:10]
        
        # Yangiklardan qidirish
        news = News.objects.filter(
            Q(title__icontains=query) | 
            Q(short_description__icontains=query) | 
            Q(category__icontains=query),
            is_published=True
        )[:10]
        
        # Materiallardan qidirish
        resources = Resource.objects.filter(
            Q(title__icontains=query) | 
            Q(description__icontains=query) | 
            Q(author__icontains=query),
            is_published=True
        )[:10]
        
        context['courses'] = courses
        context['news'] = news
        context['resources'] = resources
        context['total_results'] = courses.count() + news.count() + resources.count()
    
    return render(request, 'search_results.html', context)


@require_POST
def news_like(request, news_id):
    article = get_object_or_404(News, pk=news_id, is_published=True)
    
    # Foydalanuvchi avval layk qo'yganmi tekshirish
    liked_news = request.session.get('liked_news', [])
    
    if news_id in liked_news:
        # Laykni olib tashlash (unlike)
        article.likes_count = max(0, article.likes_count - 1)
        article.save(update_fields=['likes_count'])
        liked_news.remove(news_id)
        request.session['liked_news'] = liked_news
        
        return JsonResponse({
            'liked': False,
            'message': 'Лайк удален',
            'likes_count': article.likes_count
        })
    else:
        # Layk qo'shish
        article.likes_count += 1
        article.save(update_fields=['likes_count'])
        liked_news.append(news_id)
        request.session['liked_news'] = liked_news
        
        return JsonResponse({
            'liked': True,
            'message': 'Спасибо за ваш лайк!',
            'likes_count': article.likes_count
        })
