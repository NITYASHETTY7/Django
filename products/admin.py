from django.contrib import admin
from .models import Product
from .models import Offer

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code','discount')

admin.site.register(Product,ProductAdmin)
admin.site.register(Offer,OfferAdmin)
# Register your models here.
