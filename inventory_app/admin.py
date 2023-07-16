from typing import Any
from django.contrib import admin
from .models import (Categories, Makers, Products)


admin.site.register(
    [Categories, Makers]
)

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'product_name', 'categories', 'makers', 'product_number', 'max_inventory', 'min_inventory', 'check_inventory', 'inventory', 'reset')
    list_filter = ('user_id', 'makers', 'categories')
    list_editable = ('inventory', 'reset')
   
    #管理画面で在庫補充が必要なことを伝える
    def check_inventory(self, obj):
        if obj.inventory <= obj.min_inventory:
            count = '注文'
            return count
    check_inventory.short_description = 'ステータス'

    #在庫数のリセット
    def save_model(self, request, obj, form, change):
        if obj.reset == 1 :
            inventory = obj.max_inventory
            obj.inventory = inventory
            obj.reset = 2
        return obj.save()
