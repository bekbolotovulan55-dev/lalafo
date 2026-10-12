from os import name

from django.urls import path
from .views import CategoryListView, ProductDetailView, ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('product/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]
