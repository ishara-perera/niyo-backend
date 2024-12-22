from django.contrib import admin
from .models import Customer, Order, Design

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'address', 'email', 'phone_number', 'created_at', 'is_active')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_id', 'created_at', 'is_active')

class DesignAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_id', 'description', 'is_active')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Design, DesignAdmin)