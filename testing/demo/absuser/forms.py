# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Seller, Customer

class SellerCreationForm(UserCreationForm):
    shop_name = forms.CharField(max_length=255, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'seller'
        if commit:
            user.save()
            Seller.objects.create(user=user, shop_name=self.cleaned_data['shop_name'])
        return user


class CustomerRegistrationForm(UserCreationForm):
    address = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'customer'
        if commit:
            user.save()
            Customer.objects.create(user=user, address=self.cleaned_data['address'])
        return user
