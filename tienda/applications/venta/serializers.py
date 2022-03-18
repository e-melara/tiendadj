from rest_framework import serializers

from .models import Sale, SaleDetail

class VentaReporterSerializer(serializers.ModelSerializer):
    productos = serializers.SerializerMethodField()
    
    class Meta:
        model = Sale
        fields = (
            'id',
            'date_sale',
            'amount',
            'count',
            'type_invoce',
            'cancelado',
            'type_payment',
            'state',
            'adreese_send',
            'user',
            'productos'
        )
        
    def get_productos(self, obj):
        query = SaleDetail.objects.productos_por_venta(obj.id)
        product_serializados = DetalleVentaProductoSerializer(query, many=True).data
        
        return product_serializados
    
    
class DetalleVentaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleDetail
        fields = (
            'id',
            'sale',
            'product',
            'count',
            'price_sale',
            'price_purchase'    
        )
        
   
class ProductoDetailSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    count = serializers.IntegerField()
    

class ArrayIntergerSerializer(serializers.ListField):
    child = serializers.IntegerField()
    
        
class ProcesoVentaSerializer(serializers.Serializer):
    type_invoce = serializers.CharField()
    type_payment = serializers.CharField()
    adreese_send = serializers.CharField()
    
    # productos = ProductoDetailSerializer(many=True)
    productos = ArrayIntergerSerializer()
    cantidades = ArrayIntergerSerializer()
    
    def validate(self, data):
        if data['type_payment'] != '0':
            raise self.ValidationError('Ingrese un tipo de pago correcto')
        
        return data
    
    def validate_type_invoce(self, value):
        if value != '0':
            raise serializers.ValidationError('Ingrese un valor correcto')
        
        return value
        
        