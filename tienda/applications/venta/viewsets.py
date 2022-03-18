from django.utils import timezone
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication

from .serializers import ProcesoVentaSerializer, VentaReporterSerializer

from .models import Sale, SaleDetail
from applications.producto.models import Product

class VentaViewSets(viewsets.ViewSet):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = (TokenAuthentication, )
    queryset = Sale.objects.all()
    
    def get_permissions(self):
        if (self.action == 'retrieve') or (self.action == 'list'):
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
            
        return [permission() for permission in permission_classes]
    
    def list(self, request, *args, **kwargs):
        # queryset = Sale.objects.venta_por_usuario(self.request.user)
        queryset = Sale.objects.all()
        serializer = VentaReporterSerializer(queryset, many=True)
        
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        # venta = Sale.objects.get(id=pk)
        venta = get_object_or_404(Sale.objects.all(), pk=pk)
        serializer = VentaReporterSerializer(venta)
        
        return Response(serializer.data)
        
    def create(self, request):
        serializer = ProcesoVentaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        venta = Sale(
            count=0,
            amount = 0,
            date_sale = timezone.now(),
            type_invoce =serializer.validated_data['type_invoce'],
            type_payment=serializer.validated_data['type_payment'],
            adreese_send=serializer.validated_data['adreese_send'],
            user=self.request.user
        )
        
        amount = 0
        count = 0

        productos = Product.objects.filter(
            id__in=serializer.validated_data['productos']
        )
        cantidades = serializer.validated_data['cantidades']
        
        ventas_detalles = []
        for producto, cantidad in zip(productos, cantidades):
            venta_detalle = SaleDetail(
                sale=venta,
                product=producto,
                count=cantidad,
                price_sale = producto.price_sale,
                price_purchase=producto.price_purchase,
            )
            
            amount = amount + producto.price_sale
            count  = count + cantidad
            
            ventas_detalles.append(venta_detalle)
            
        venta.count = count
        venta.amount = amount
        
        venta.save()
        
        SaleDetail.objects.bulk_create(ventas_detalles)
        
        return Response({
            'success': 'ok'
        })
