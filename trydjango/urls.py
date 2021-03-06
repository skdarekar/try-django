"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import home_view, contact_view, about_view, social_view
from products.views import (product_detail_view, product_create_view, render_initial_view, 
dynamic_lookup_view, delete_product_view, preview_products_list)

urlpatterns = [
    path('', home_view, name="home"),
    path('home/', home_view, name='home'),
    path('contact/', contact_view),
    path('about/', about_view),
    path('social/', social_view),
    path('product/', product_detail_view),
    path('product/<int:my_id>', dynamic_lookup_view),
    path('product/<int:my_id>/delete/', delete_product_view),
    path('product/create', product_create_view),
    path('product/initial', render_initial_view),
    path('product/list', preview_products_list),
    path('admin/', admin.site.urls),
]
