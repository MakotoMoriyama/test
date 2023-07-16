from typing import Any, Callable, Dict
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, FormView ,DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from .forms import ProductRegistFrom, InvetoryUpdateFrom
import os
from .models import(
    Products, 
)
from django.urls import reverse_lazy

class ProductListView(LoginRequiredMixin, ListView):
    model = Products
    template_name = os.path.join('inventory_app', 'product_list.html')

    def get_queryset(self):
        query = super().get_queryset()
        categories_category_name = self.request.GET.get('categories_category_name')
        makers_maker = self.request.GET.get('makers_maker')
        a = 1 #ログイン中のユーザーのデータを表示
        if a == 1:
            query = query.filter(user_id=self.request.user)

        if categories_category_name:
            query = query.filter(
                categories__category_name = categories_category_name
            )
        if makers_maker:
            query = query.filter(
                makers__maker=makers_maker
            )
        #昇順・降順
        order_by_inventory = self.request.GET.get('order_by_inventory', 0)
        if order_by_inventory == '1':
            query = query.order_by('inventory')
        elif order_by_inventory == '2':
            query = query.order_by('-inventory')   
        return query
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories_category_name'] = self.request.GET.get('categories_category_name', '')
        context['makers_maker'] = self.request.GET.get('makers_maker', '')
        order_by_inventory = self.request.GET.get('order_by_inventory', 0)
        if order_by_inventory == '1':
            context['ascending'] = True
        elif order_by_inventory == '2':
            context['descending'] = True
        return context
    
# 在庫部品の登録
class ProductRegistView(LoginRequiredMixin, CreateView):
    model = Products
    template_name = os.path.join('inventory_app', 'product_regist.html')
    form_class = ProductRegistFrom

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.inventory = obj.max_inventory
            obj.user_id_id = request.user.id
            obj.save()
        return redirect('/inventory_app/product_regist/', pk=obj.pk)

        
#在庫部品の削除
class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Products
    template_name = os.path.join('inventory_app', 'delete_product.html')
    success_url = '/inventory_app/product_list/'



#在庫数の変更
class InvetoryUpdateView(LoginRequiredMixin, UpdateView):
    template_name =  os.path.join('inventory_app', 'update_inventory.html')
    model = Products
    success_url = '/inventory_app/product_list/'
    form_class = InvetoryUpdateFrom



