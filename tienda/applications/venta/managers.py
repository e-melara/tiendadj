from django.db import models

class SaleDetailManager(models.Manager):
    def productos_por_venta(self, venta_id):
        return self.filter(
            sale_id=venta_id,
        )
        
        
class SaleManager(models.Manager):
    def venta_por_usuario(self, usuario):
        return self.filter(
            user=usuario
        )