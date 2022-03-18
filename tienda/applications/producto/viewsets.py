from rest_framework import viewsets
from rest_framework.response import Response

from .models import Colors, Product

# serializers colors
from .serializers import (
    ColorSerializer, PaginationSerializer,
    ProductSerializerViewSet
)

class ColorViewSet(viewsets.ModelViewSet):
    serializer_class = ColorSerializer
    queryset = Colors.objects.all()
    
    
class ProductoViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializerViewSet
    queryset = Product.objects.all()
    pagination_class = PaginationSerializer
    
    def perform_create(self,serializer):
        serializer.save(
            video="https://youtu.be/xvVLWSsKjkI"
        )

    def list(self, request, *args, **kwargs):
        queryset = Product.objects.productos_por_user(self.request.user)
        serializer = self.get_serializer(queryset, many=True)
        
        return Response(serializer.data)