from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    pass


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    address = models.CharField(verbose_name=_('Address'), max_length=255, blank=True, null=True)
    phone_number = models.CharField(verbose_name=_('Phone Number'), max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)

    def __str__(self):
        return f'{self.id} - {self.user.get_full_name()}'


class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    customer = models.ForeignKey(Customer, verbose_name=_('Customer'), on_delete=models.CASCADE)
    status = models.CharField(verbose_name=_('Status'), max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)

    def __str__(self):
        return f'Order {self.id} by {self.customer.user.username}'

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class Design(models.Model):
    order = models.ForeignKey(Order, verbose_name=_('Order'), on_delete=models.CASCADE, related_name='designs')
    design_img = models.ImageField(verbose_name=_('Design Image'), upload_to='designs/', blank=True, null=True)
    description = models.TextField(verbose_name=_('Description'))
    created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
    is_active = models.BooleanField(verbose_name=_('Is Active'), default=True)

    def __str__(self):
        return f'Design {self.id} for Order {self.order.id}'
