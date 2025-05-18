from django.urls import path
from . import views

urlpatterns = [
    path('', views.appointment_list, name='appointment_list'),
    path('new/', views.appointment_create, name='appointment_create'),
    path('edit/<int:pk>/', views.appointment_update, name='appointment_update'),
]
