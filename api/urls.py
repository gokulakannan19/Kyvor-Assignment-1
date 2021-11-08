from django.urls import path
from .import views

urlpatterns = [
    path('', views.get_routes, name="get-routes"),
    path('patients/', views.get_patients, name="get-patients"),
    path('patient-create/', views.patient_create, name="patient-create"),
    path('patient-update/<str:pk>/', views.patient_update, name="patient-update"),
    path('patient-delete/<str:pk>/', views.patient_delete, name="patient-delete"),
]
