from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(verbose_name='First Name', max_length=255, blank=True, null=True)
    last_name = models.CharField(verbose_name='Last Name',max_length=255, blank=True, null=True)
    address = models.CharField(verbose_name='Address',max_length=255, blank=True, null=True) 
    email = models.CharField(verbose_name='Email', max_length=255, blank=True, null=True) 
    phone_number = models.CharField(verbose_name='Phone Number', max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Created At', auto_now_add=True)
    is_active = models.BooleanField(verbose_name='Is Active', default=True)

    def __str__(self):
        return f'{self.id} - {self.first_name} {self.last_name}'
        

class Order(models.Model):
    customer_id = models.ForeignKey(Customer, verbose_name='Customer ID', on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='Created At', auto_now_add=True)
    is_active = models.BooleanField(verbose_name='Is Active', default=True)

    def __str__(self):
        return f'{self.id}'

class Design(models.Model):
    order_id = models.ForeignKey(Order, verbose_name='Order ID', on_delete=models.CASCADE)
    design_img = models.CharField(verbose_name='Design Image', max_length=2000, blank=True, null=True)
    description = models.TextField(verbose_name='Description')
    created_at = models.DateTimeField(verbose_name='Created At', auto_now_add=True)
    is_active = models.BooleanField(verbose_name='Is Active', default=True)