from django.contrib import admin

# Register your models here.
from .models import Product

class Productadmin(admin.ModelAdmin):
    list_display = ('id','name','price')
    search_fields = ('name',)

admin.site.register(Product,Productadmin)

