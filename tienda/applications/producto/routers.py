from rest_framework.routers import DefaultRouter

# applications local
from . import viewsets

# creamos el router default
router = DefaultRouter()
router.register(r'colors', viewsets.ColorViewSet, basename="colors")
router.register(r'productos', viewsets.ProductoViewSet, basename="productos")

urlpatterns = router.urls