from django.urls import path
from .import views

urlpatterns = [
    path('', views.get_genes, name="home"),
    path('gene/<str:pk>/', views.gene_detail, name="gene-detail"),
    path('variant/<str:pk>/', views.variant_detail, name="variant-detail")
]
