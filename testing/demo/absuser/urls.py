# urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('create-seller/', views.create_seller, name='create_seller'),
    path('customer-registration/', views.customer_registration, name='customer_registration'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),
    path('create_product/', views.create_product, name='create_product'),
    path('customer_page',views.customer_page,name="customer_page"),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
