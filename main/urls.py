from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('news/', views.news, name='news'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
    path('news/<int:news_id>/like/', views.news_like, name='news_like'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('resources/', views.resources, name='resources'),
    path('search/', views.search, name='search'),
]

