import objects
from django.shortcuts import render, redirect, get_object_or_404

from .models import Customer, Product


# Create your views here.


def customer_list_view(request):
    customers = Customer.objects.all()

    return render(request, 'hesabdari/customer_list.html', context={"customers": customers})


def add_customer_view(request):
    products = Product.objects.all()
    # customerr = Customer.objects.customer_javad() شخصی سازی متد ها

    if request.method == "POST":
        name = request.POST.get('name')
        phone_number = request.POST.get('number')
        new_customer = Customer.objects.create(name=name, phone_number=phone_number)
        return redirect("hesabdari:customerlist")
    return render(request, "hesabdari/add_customer.html", context={ "prosucts": products})


def customer_taki_view(request, id):
    customerr = get_object_or_404(Customer, id=id)
    product = Product.objects.all()
    if request.method == "GET":
        name_product = request.GET.get('serch')
        if name_product:
            product_search = Product.objects.filter(name=name_product)

            return render(request, 'hesabdari/customer_taki.html',
                          context={"cotomer": customerr, "product_search": product_search})

    return render(request, 'hesabdari/customer_taki.html',
                  context={"cotomer": customerr, "products": product})


def delete_customer(request, id):
    del_customer = Customer.objects.get(id=id)
    del_customer.delete()

    return redirect('hesabdari:customerlist')


def add_product_view(request):

    if request.method == "POST":
        name_product = request.POST.get('name')
        price_product = request.POST.get('price')
        new_product = Product.objects.create(name=name_product,price_product=price_product)
        return redirect("hesabdari:productlist")

    return render(request, 'hesabdari/add_product.html',)


def delete_product_view(request, id):
    del_product = Product.objects.get(id=id)
    del_product.delete()
    return redirect("hesabdari:productlist")


def list_product_view(request):
    products = Product.objects.all()
    return render(request, 'hesabdari/product_list.html',context={"products" : products})
