from django.db import models

# Create your models here.
class Stock(models.Model):
    categoria = models.CharField(max_length=50, blank=True, null=True)
    peso = models.IntegerField(default='0', blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    objeto_nombre = models.CharField(max_length=50, blank=True, null=True)
    cantidad = models.IntegerField(default='0',blank=True, null=True)
    recibir_cantidad = models.IntegerField(default='0', blank=True, null=True)
    recibir_de = models.CharField(max_length=50, blank=True, null=True)
    usado_cantidad = models.IntegerField(default='0', blank=True, null=True)
    usado_por = models.CharField(max_length=50, blank=True, null=True)
    usado_para = models.CharField(max_length=50, blank=True, null=True)
    numero = models.CharField(max_length=50, blank=True, null=True)
    creado_por = models.CharField(max_length=50, blank=True, null=True)
    reorden_nivel = models.IntegerField(default='0', blank=True, null=True)
    ultima_actualizacion = models.DateTimeField(auto_now_add=False, auto_now=True)
    exportar_a_CSV = models.BooleanField(default=False)

    def __str__(self):
        return self.objeto_nombre + ' ==> ' + str(self.cantidad)