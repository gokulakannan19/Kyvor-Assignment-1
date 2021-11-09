from django.urls import path
from .import views

urlpatterns = [
    path('', views.gene_list, name="home"),
    path('gene-detail/<str:pk>/', views.gene_detail, name="gene-detail"),
    path('variant-detail/<str:pk>/', views.variant_detail, name="variant-detail"),
]
