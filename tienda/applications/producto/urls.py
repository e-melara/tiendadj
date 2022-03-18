from django.urls import path
from . import views

urlpatterns = [
    path('api/product/por-usuario', views.ListProductView.as_view(), name='api-producto-usuario'),
    path('api/product/genero/<genere>/', views.ListProductGeneroView.as_view(), name='api-producto-genero'),
    path('api/product/filtrar/', views.FiltrarProductos.as_view(), name='api-producto-filtrar'),
]

