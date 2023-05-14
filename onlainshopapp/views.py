from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse

# Create your views here.
def show_cataloug(request):
    response = render(request,"catalog.html",context={'products': Product.objects.all()})
    if request.method == "POST":
        if "product" not in request.COOKIES: #Якщо в запиті немає файлу cookie 'product_pk'
            new_product = request.POST.get('product_pk') + '_' + request.POST.get('amount')
            response.set_cookie('product', new_product) #Встановлюе cookie 'product_pk' зі значенням new_product
            return response #Повернути 
        else: #Якщо в запиті є файл cookie 'product_pk'
            can_else = True
            products = request.COOKIES['product'].split(' ')
            for product in products:
                index = products.index(product)
                product = product.split('_')
                products[index] = product
            for product in products:
                if request.POST.get('product_pk') in product[0]:
                    index = products.index(product)
                    products[index][1] = str(int(products[index][1])+ int(request.POST.get('amount')))
                    products= " ".join("_".join(product) for product in products)
                    response.set_cookie('product', products)
                    can_else = False
                    return response 

            if can_else:
                new_product = request.COOKIES['product'] + " " + request.POST.get('product_pk') + '_' + request.POST.get('amount')
                response.set_cookie('product',new_product) ##Встановлюе cookie 'product_pk' зі значенням new_product
                return response           
    return response

def show_cart(request):
    if "product" in request.COOKIES: #
        products = request.COOKIES['product'].split(' ')
        for product in products:
            index = products.index(product)
            product = product.split('_')
            products[index] = product
        for product in products:
            index = products.index(product)
            product[0] = Product.objects.get(pk= int(product[0]) )
            products[index][0] = product[0]
        response = HttpResponse("work")
        responses = render(request,"cart.html",context={"products": products})
    else:
        responses = render(request,"cart.html",context={"products": []})
    if request.method == "POST":
        products = request.COOKIES['product'].split(' ')
        if request.POST.get('name') == 'delete':
            if len(request.COOKIES['product'].split(' ')) > 1:
                product = request.POST.get('item') + "_" + request.POST.get('amount')
                products.remove(product)
                products = " ".join(products)
                print(products)
                response.set_cookie('product', products)
                return response
            else:
                response.delete_cookie('product')
                return response
        if request.POST.get('name') == 'minus':
            
            product_minus = request.POST.get('item') + "_" + request.POST.get('amount')
            index_num = products.index(product_minus)
            for product in products:
                index = products.index(product)
                product = product.split('_')
                products[index] = product
            if int(products[index_num][1]) - 1 <= 0:
                if len(request.COOKIES['product'].split(" ")) == 1:
                    response.delete_cookie('product')
                    return response
                else:
                    del products[index_num]
                    products= " ".join("_".join(product) for product in products) 
                    response.set_cookie('product', products)
                    return response
            else:
                products[index_num][1] = str(int(products[index_num][1]) - 1)
                products= " ".join("_".join(product) for product in products) 
                response.set_cookie('product', products)
                return response
        if request.POST.get('name') == 'plus':
            product_plus = request.POST.get('item') + "_" + request.POST.get('amount')
            index_num = products.index(product_plus)
            for product in products:
                index = products.index(product)
                product = product.split('_')
                products[index] = product
            products[index_num][1] = str(int(products[index_num][1]) + 1)
            products= " ".join("_".join(product) for product in products) 
            response.set_cookie('product', products)
            return response   
    return responses 
    