import objects
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AddCustomer, AddProduct
from .models import Customer, Product


# Create your views here.


def customer_list_view(request):
    customers = Customer.objects.all()

    return render(request, 'hesabdari/customer_list.html', context={"customers": customers})


def add_customer_view(request):
    if request.method == "POST":
        form = AddCustomer(request.POST)
        if form.is_valid():
            Customer.objects.create(name=form.cleaned_data["name"], phone_number=form.cleaned_data["phonenumber"])
            return redirect("hesabdari:customerlist")
    else:
        form = AddCustomer()

    return render(request, "hesabdari/add_customer.html", context={"form": form})


def customer_taki_view(request, id):
    customerr = get_object_or_404(Customer, id=id)
    product = Product.objects.all()
    if request.method == "POST":
        for i in product:
            choiceproduct = request.POST.get(i.name)
            if choiceproduct is not None:
                customerr.product.add(Product.objects.get(id=choiceproduct))

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
        form = AddProduct(request.POST)
        if form.is_valid():
            Product.objects.create(name=form.cleaned_data["name"], price_product=form.cleaned_data["price_product"])
            return redirect("hesabdari:productlist")
    else:
        form = AddProduct()

    return render(request, 'hesabdari/add_product.html', {"form": form})


def delete_product_view(request, id):
    del_product = Product.objects.get(id=id)
    del_product.delete()
    return redirect("hesabdari:productlist")


def list_product_view(request):
    products = Product.objects.all()
    return render(request, 'hesabdari/product_list.html', context={"products": products})
