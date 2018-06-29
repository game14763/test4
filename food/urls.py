from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    path('menu/', views.menu, name='menu'),
]
