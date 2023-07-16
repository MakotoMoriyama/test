from django.urls import path
from .views import (
    ProductListView, ProductRegistView, InvetoryUpdateView, 
    ProductDeleteView
)

app_name='inventory_app'
urlpatterns = [
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product_regist/', ProductRegistView.as_view(), name='product_regist'),
    path('update_inventory/<int:pk>', InvetoryUpdateView.as_view(), name='update_inventory'),
    path('delete_product/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
]