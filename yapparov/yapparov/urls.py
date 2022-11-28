from django.urls import path
from info import views

urlpatterns = [
    path('', views.index),
    path('error', views.error, name='error'),
    path("user", views.user),
    path("user/<login>", views.user),
    path("user/<login>/<name>", views.user),
    path("user/<login>/<name>/<int:num>", views.user),
]
