from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    category_image = models.ImageField(upload_to = 'category_photo/')

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.PositiveSmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    phone_number = PhoneNumberField()
    city = models.CharField(max_length=40)
    type = models.BooleanField(default=False)
    product_image = models.ImageField(upload_to = 'product_photo/', null=True, blank=True)
    descriptions = models.TextField(null=True, blank=True)
    number_product = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product_name} - {self.price}'
