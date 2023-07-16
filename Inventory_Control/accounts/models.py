from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin)
from django.urls import reverse_lazy


class UserManager(BaseUserManager):
    def create_user(self, user_name, email, password=None):
        if not user_name:
            raise ValueError('Enter Username')
        if not email:
            raise ValueError('Enter Email')
        user = self.model(
            user_name = user_name,
            email = email
        )
        user.set_password(password)
        user.save(using=self._db)
        return user  
    
    def create_superuser(self, user_name, email, password=None):
        user = self.model(
            user_name = user_name,
            email = email,
        )
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    
#カスタマイズ用ユーザーの作成
class Users(AbstractBaseUser, PermissionsMixin):
    user_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=255, unique=True)
    tel_number = models.CharField(max_length=255) 
    address = models.CharField(max_length=255) 
    select_holiday = [
        (1, '日曜日'),
        (2, '月曜日'),
        (3, '火曜日'),
        (4, '水曜日'),
        (5, '木曜日'),
        (6, '金曜日'),
        (7, '土曜日'),
    ]
    regular_holiday = models.IntegerField(choices=select_holiday, null=True) 
    business_hours = models.CharField(max_length=255, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True) 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    objects = UserManager()

    def get_absolute_url(self):
        return reverse_lazy('accounts:top')
    
    class Meta:
        verbose_name_plural = 'ユーザー'

    def __str__(self):
        return self.user_name
        

