from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('schedule', views.schedule, name='schedule'),
    path('map', views.map, name='map'),
    path('message/', views.message, name='message'),
    path('message/<int:page>', views.message, name='message'),
    path('trainer', views.trainer, name='trainer'),
    ]

