from django.shortcuts import render
from django.views.generic import ListView
from home.models import Product, Order, ProductSold
from django.db.models import Q
import json
import datetime



def homeview(request):
    with open('data.json', 'r+') as f:
        data = json.load(f)

    # y = ProductSold.objects.get(id=1)
    # aa =ProductSold.objects.get(id=2)
    # x = Order.objects.create(
    #     status='Finalizado',
    #     date=datetime.datetime.now(),
    #     total=10.00,
    # )
    # x.save()
    # x.product_sold.add(y)
    # x.product_sold.add(aa)
    eita = Order.objects.all()
    ob = Product.objects.all()
    ab = ProductSold.objects.all()

    for i in eita:
        print(i.product_sold.quantity)
    # for i in data['Orders']:
    #     print(i['Order']['ProductsSold'])
    #     sku = i['Order']['ProductsSold'][0]['ProductsSold']['sku']
    #     name = i['Order']['ProductsSold'][0]['ProductsSold']['name']
    #     quantity = i['Order']['ProductsSold'][0]['ProductsSold']['quantity']
    #     price = float(i['Order']['ProductsSold'][0]['ProductsSold']['price']) / int(quantity)
    #     cost_price = i['Order']['ProductsSold'][0]['ProductsSold']['cost_price']

        # print(sku, name, quantity, price, cost_price) 

        
    return render(request, template_name='index.html', context={'data': ob, 'ab':ab, 'eita': eita})

# Create your views here.
# class HomeAPIView(ListView):

    

