from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Category, Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ProductForm
from django.urls import reverse_lazy, reverse

class CategoryListView(ListView):
    queryset = Category.objects.all()
    context_object_name = 'categories'
    template_name = 'category_list.html'



class ProductListView(ListView):
    queryset = Product.objects.all()
    context_object_name = 'products'
    template_name = 'product_list.html'



class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    context_object_name = 'product'
    template_name = 'product_detail.html'

class ProductCreateView(CreateView):
    context_object_name = 'product'
    form_class = ProductForm
    template_name = 'product_create.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    queryset = Product.objects.all()
    template_name = 'product_update.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})

class ProductDeleteView(DeleteView):
    queryset = Product.objects.all()
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')


