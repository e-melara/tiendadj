from django.urls import path

from . import views

urlpatterns = [
    path('api/sale/list/', view=views.ReporteVentasList.as_view(), name='sale-list'),
    path('api/venta/create/', view=views.RegistrarVenta.as_view(), name='sale-create'),
]
