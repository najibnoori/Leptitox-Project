from django.contrib import admin
from django.urls import path
from .views import newsletter_subscribe, newsletter_unsubscribe, send_newsletter

app_name = 'newsletter'
urlpatterns = [
    path('subscribe/', newsletter_subscribe, name='subscribe'),
    path('unsubscribe/', newsletter_unsubscribe, name='unsubscribe'),
    path('send/', send_newsletter, name='send_newsletter'),
]
