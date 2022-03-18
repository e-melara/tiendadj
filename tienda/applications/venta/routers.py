from rest_framework.routers import DefaultRouter

from . import viewsets

router = DefaultRouter()
router.register(r'ventas', viewsets.VentaViewSets, basename="ventas")

urlpatterns = router.urls