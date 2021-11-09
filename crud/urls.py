from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="patient"),
    path('add/', views.add_patient, name="add-patient"),
    path('update/<str:pk>/', views.update_patient, name="update-patient"),
    path('delete/<str:pk>/', views.delete_patient, name="delete-patient"),
]
