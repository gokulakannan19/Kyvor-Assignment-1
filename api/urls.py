from django.urls import path
from .import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', views.get_routes, name="get-routes"),


    path('patients/', views.get_patients, name="get-patients"),
    path('patient-create/', views.patient_create, name="patient-create"),
    path('patient-update/<str:pk>/', views.patient_update, name="patient-update"),
    path('patient-delete/<str:pk>/', views.patient_delete, name="patient-delete"),
]
