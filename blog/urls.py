from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.allblogs, name = 'blog'),
    path('<int:blog_id>/',views.detail, name = 'detail'),
]