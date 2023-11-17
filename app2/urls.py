from django.urls import path
from .views import *
app_name='teja'
urlpatterns=[
    path('data_render/',data_render,name='data_render'),
]