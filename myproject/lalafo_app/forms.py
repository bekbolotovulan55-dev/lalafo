from .models import Category, Product
from django.forms import ModelForm


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['product_name','price','category','phone_number',
                  'city','type','product_image','descriptions','number_product']