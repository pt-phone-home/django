from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from second_app import views

urlpatterns = [
    path('', views.list, name='list'),
    # path('', views.index, name='index'),
    path('', views.sign_up, name='sign_up'),
    path('', views.drinks, name='drinks')
]