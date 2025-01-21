
from django.contrib import admin
from .models import User, Seller, Customer

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_type')

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('user', 'shop_name')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'address')
