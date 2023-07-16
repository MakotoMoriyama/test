from django.contrib import admin
from .models import Users
from django.contrib.auth.models import Group

admin.site.unregister(Group)  

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'email', 'address', 'regular_holiday',)