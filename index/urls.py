from django.urls import path
from . import views

app_name = 'index'

urlpatterns = [
    path('', views.index_url, name='index_url'),
    path('Speaker/', views.index_detail, name='index_detail'),
    path('index/', views.index, name='index_index'),
    path('schedule/', views.schedule, name='index_schedule'),
]