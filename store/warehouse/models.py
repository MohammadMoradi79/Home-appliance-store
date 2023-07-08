from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE, related_name='children')

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    last_update = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    class Meta:
        ordering = ['first_name', 'last_name']

