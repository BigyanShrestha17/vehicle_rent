from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('gallery/', views.gallery, name='gallery'),
    path('client/', views.client, name='client'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('book_now/', views.book_now, name='book_now'),
]
