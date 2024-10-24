from django.db import models
from django.db.models.signals import pre_save 
from django.dispatch import receiver
from medi_book.utils import *

class MedicineModel(models.Model):
    name = models.CharField(max_length=150)
    generic_name = models.CharField(max_length=150)
    manufacturer = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    price = models.IntegerField()
    batch_number = models.CharField(max_length=50)
    form = models.CharField(max_length=100)
    stock_quantity = models.IntegerField()
    slug = models.SlugField(unique=True, null=True)


@receiver(pre_save, sender=MedicineModel) 
def pre_save_receiver(sender, instance, *args, **kwargs): 
    if not instance.slug: 
        instance.slug = unique_slug_generator(instance) 
  


    
  
