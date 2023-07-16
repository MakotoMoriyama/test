from django.db import models
from accounts.models import Users


class Categories(models.Model):
    category_name = models.CharField(max_length=255, verbose_name = 'カテゴリー')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True) 
    class Meta:
        db_table = 'categories'
        verbose_name_plural = 'カテゴリー'

    def __str__(self):
        return self.category_name

class Makers(models.Model):
    maker = models.CharField(max_length=255, verbose_name = 'メーカー名')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True) 

    class Meta:
        db_table = 'makers'
        verbose_name_plural = 'メーカー'

    def __str__(self):
        return self.maker
    

class Products(models.Model): 
    product_name = models.CharField(max_length=255, verbose_name='部品名')
    product_number = models.CharField(max_length=255, verbose_name='品番')
    max_inventory = models.IntegerField(verbose_name='最大在庫数')
    min_inventory = models.IntegerField(verbose_name='最小在庫数')
    inventory = models.IntegerField(default=0, verbose_name='在庫数')
    check_reset = [
        (1, 'リセット'),
        (2, '-')
    ]
    reset = models.IntegerField(choices=check_reset, default=2, verbose_name='リセット')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True) 
    categories = models.ForeignKey(
        Categories, on_delete=models.CASCADE,
        null=True, verbose_name='カテゴリー'
    )
    makers = models.ForeignKey(
        Makers, on_delete=models.CASCADE,
        null=True, verbose_name='メーカー'
    )
    user_id = models.ForeignKey(
        Users, on_delete=models.CASCADE,
        null=True, verbose_name='ユーザー'
    )

    class Meta:
        db_table = 'product'
        verbose_name_plural = '在庫管理'


    def __str__(self):
        return self.product_number
    


