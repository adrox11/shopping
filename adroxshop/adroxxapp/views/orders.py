from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from adroxxapp.models.customer import Customer
from django.views import View

from adroxxapp.models.product import Product
from adroxxapp.models.orders import Order




class OrderView(View):


    def get(self , request ):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request , 'orders.html'  , {'orders' : orders})
