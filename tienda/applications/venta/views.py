from django.utils import timezone

from rest_framework.response import Response
# Create your views here.
from rest_framework.generics import (
    ListAPIView, CreateAPIView
)


from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


from .models import Sale, SaleDetail
from applications.producto.models import Product


from .serializers import (
    VentaReporterSerializer,
    ProcesoVentaSerializer
)

class ReporteVentasList(ListAPIView):
    serializer_class = VentaReporterSerializer
    
    def get_queryset(self):
        return Sale.objects.all()
    

class RegistrarVenta(CreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    serializer_class = ProcesoVentaSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = ProcesoVentaSerializer(data=request.data)       
        serializer.is_valid(raise_exception=True)
        venta = Sale.objects.create(
            count=0,
            amount = 0,
            date_sale = timezone.now(),
            type_invoce =serializer.validated_data['type_invoce'],
            type_payment=serializer.validated_data['type_payment'],
            adreese_send=serializer.validated_data['adreese_send'],
            user=self.request.user
        )
        # monto y cantidad 
        amount = 0
        count = 0
        # recuperamos los productos de la venta
        # productos = serializer.validated_data['productos']
        productos = Product.objects.filter(
            id__in=serializer.validated_data['productos']
        )
        cantidades = serializer.validated_data['cantidades']
        
        ventas_detalles = []
        for p, cantidad in zip(productos, cantidades):
            venta_detalle = SaleDetail(
                sale=venta,
                product=p,
                count=cantidad,
                price_purchase=p.price_purchase,
                price_sale=p.price_sale
            )
            amount = amount + p.price_sale
            count = count + cantidad
            
            ventas_detalles.append(venta_detalle)
            
        venta.amount = amount
        venta.count = count
        venta.save()
        
        SaleDetail.objects.bulk_create(ventas_detalles)
            
        return Response({
            "code":'ok'
        })