
from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from WebApp.models.customer import Customer
from django.views import  View
from WebApp.models.product import Products

class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Products.get_products_by_id(ids)
        print(products)
        return render(request , 'MyApp/cart.html' , {'products' : products} )