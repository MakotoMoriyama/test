from typing import Any, Dict
from django import forms
from .models import Products
from django.utils import timezone
from datetime import datetime
from django.shortcuts import get_object_or_404

#部品登録
class ProductRegistFrom(forms.ModelForm):

    class Meta:
        model = Products     
        exclude = ['create_at', 'update_at', 'inventory', 'user_id', 'reset']
        labels = {
            'product_name': '部品名',
            'product_number': '品番',
            'max_inventory': '最大在庫数',
            'min_inventory': '最小在庫数',
            'categories': 'カテゴリー',
            'makers': 'メーカー',
        }

#在庫更新
class InvetoryUpdateFrom(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput())
    inventory = forms.IntegerField(label='在庫数')

    class Meta:
        model = Products
        fields = ['id','inventory']

