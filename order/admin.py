from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import User, Customer, Order, Design


# Register your models here.

@admin.register(User)
class User(ImportExportModelAdmin):
    pass


@admin.register(Customer)
class Customer(ImportExportModelAdmin):
    pass


@admin.register(Order)
class Order(ImportExportModelAdmin):
    pass


@admin.register(Design)
class Design(ImportExportModelAdmin):
    pass
