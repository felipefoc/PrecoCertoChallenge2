from django.db import models


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    cost_price = models.DecimalField(max_digits=8, decimal_places=2)

class ProductSold(models.Model):
    sku = models.CharField(max_length=100,default=f'P{id}')
    quantity = models.IntegerField()
    name = models.ForeignKey(Product, on_delete=models.CASCADE)
    cost_price = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cost_prices')


class Order(models.Model):

    CHOICES = [
        ('Finalizado', 'Finalizado'),
        ('Pendente', 'Pendente'),
    ]
    status = models.CharField(max_length=100, null=False, choices=CHOICES)
    date = models.DateField()
    total = models.DecimalField(max_digits=8, decimal_places=2)
    product_sold = models.ManyToManyField(ProductSold, through='Product')
