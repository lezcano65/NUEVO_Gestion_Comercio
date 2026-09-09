from django.contrib import admin
from .forms import StockCreateForm
# Register your models here.
from .models import Stock

class StockCreateAdmin(admin.ModelAdmin):
    list_display = ['objeto_nombre', 'cantidad','categoria','descripcion']
    form = StockCreateForm
    list_filter = ['categoria']
    search_fields = ['objeto_nombre', 'cantidad']

admin.sites.site.register(Stock, StockCreateAdmin)# primero el Base y segundo parametro el personalizado de arriba