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
    path('genes/', views.genes, name="genes"),
    path('get-genes/', views.get_genes, name="get-genes"),
    path('gene-create/', views.gene_create, name="gene-create"),
    path('gene-detail/<str:pk>/', views.gene_detail, name="gene-detail"),
    path('variant-detail/<str:pk>/', views.variant_detail, name="variant-detail"),

    path('patients/', views.get_patients, name="get-patients"),
    path('patient-create/', views.patient_create, name="patient-create"),
    path('patient-update/<str:pk>/', views.patient_update, name="patient-update"),
    path('patient-delete/<str:pk>/', views.patient_delete, name="patient-delete"),
]
