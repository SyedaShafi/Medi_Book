from django.contrib import admin
from .models import MedicineModel
# Register your models here.
class MedicineModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']

admin.site.register(MedicineModel, MedicineModelAdmin)
