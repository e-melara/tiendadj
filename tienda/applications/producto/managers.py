from django.db import models


class ProductoManager(models.Manager):
    def productos_por_user(self, usuario):
        return self.filter(
            user_created=usuario
        )
        
    def productos_por_genero(self, genero):
        if genero == 'm':
            man = True
            woman = False
        else:
            woman = True
            man = False
            
        return self.filter(
            man=man,
            woman=woman
        )
        
        
    def filtrar_productos(self, **filtros):
        return self.filter(
            man=filtros['man'],
            woman=filtros['woman'],
            name__icontains=filtros['name']
        )
