from msilib.schema import ListView

import objects
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, FormView, DetailView

from .forms import AddCustomer, AddProduct
from .models import Customer, Product


# Create your views here.
class CustomerListView(ListView):
    model = Customer
    template_name = 'hesabdari/customer_list.html'
    context_object_name = "customers"
    queryset = None

    def get(self, request, *args, **kwargs):
        customers = Customer.objects.all()

        name_search = request.GET.get("searchname")
        if name_search:
            print(name_search)
            customers_search = Customer.objects.filter(name__contains=name_search)
            return render(request, self.template_name,
                          {self.context_object_name: customers_search, })
        else:
            return render(request, self.template_name, {self.context_object_name: customers})


# def add_customer_view(request):
#     if request.method == "POST":
#         form = AddCustomer(request.POST)
#         if form.is_valid():
#             Customer.objects.create(name=form.cleaned_data["name"], phone_number=form.cleaned_data["phonenumber"])
#             return redirect("hesabdari:customerlist")
#     else:
#         form = AddCustomer()

class AddCustomerView(FormView):
    template_name = "hesabdari/add_customer.html"
    form_class = AddCustomer
    success_url = reverse_lazy("hesabdari:customerlist")

    def form_valid(self, form):
        data = form.cleaned_data
        Customer.objects.create(name=data["name"],
                                phone_number=data["phonenumber"])
        return super().form_valid(form)


def deleteproductcustomer(request, idproduct, idcustomer):
    customer = Customer.objects.get(id=idcustomer)
    customer.product.remove(Product.objects.get(id=idproduct))
    return redirect('hesabdari:coustomer_taki', id=idcustomer)


class CustomerDetailView(DetailView, ):
    model = Customer
    pk_url_kwarg = "id"
    template_name = "hesabdari/customer_taki.html"
    context_object_name = "cotomer"

    def get_context_data(self, **kwargs):
        context = super(CustomerDetailView, self).get_context_data()
        return context

    def post(self, request, *args, **kwargs):
        customerr = get_object_or_404(Customer, id=self.kwargs["id"])
        list_prices = 0
        for i in customerr.product.all():
            list_prices += i.price_product
            customerr.all_costs = list_prices
        for i in Product.objects.all():
            choiceproduct = request.POST.get(i.name)
            if choiceproduct is not None:
                customerr.product.add(Product.objects.get(id=choiceproduct))
        return render(request, self.template_name,
                      {self.context_object_name: customerr, "products": Product.objects.all(),
                       "list_prices": list_prices})

    def get(self, request, *args, **kwargs):
        global list_price
        customerr = get_object_or_404(Customer, id=self.kwargs["id"])
        list_prices = 0

        for i in customerr.product.all():
            list_prices += i.price_product
            customerr.all_costs = list_prices

        searchword = request.GET.get("serch")
        if searchword:
            products_search = Product.objects.filter(name__contains=searchword)
            return render(request, 'hesabdari/customer_taki.html',
                          context={"cotomer": customerr, "product_search": products_search, "list_prices": list_prices,
                                   })
        return render(request, 'hesabdari/customer_taki.html',
                      context={"cotomer": customerr, "products": Product.objects.all(), "list_prices": list_prices})


# def customer_taki_view(request, id):
#     customerr = get_object_or_404(Customer, id=id)
#     product = Product.objects.all()
#     if request.method == "POST":
#         for i in product:
#             choiceproduct = request.POST.get(i.name)
#             if choiceproduct is not None:
#                 print(choiceproduct)
#                 customerr.product.add(Product.objects.get(id=choiceproduct))
#
#     if request.method == "GET":
#         name_product = request.GET.get('serch')
#         if name_product:
#             product_search = Product.objects.filter(name__contains=name_product)
#
#             return render(request, 'hesabdari/customer_taki.html',
#                           context={"cotomer": customerr, "product_search": product_search})
#
#     return render(request, 'hesabdari/customer_taki.html',
#                   context={"cotomer": customerr, "products": product})


def delete_customer(request, id):
    del_customer = Customer.objects.get(id=id)
    del_customer.delete()

    return redirect('hesabdari:customerlist')


# def add_product_view(request):
#     if request.method == "POST":
#         form = AddProduct(request.POST)
#         if form.is_valid():
#             Product.objects.create(name=form.cleaned_data["name"], price_product=form.cleaned_data["price_product"])
#             return redirect("hesabdari:productlist")
#     else:
#         form = AddProduct()
#
#     return render(request, 'hesabdari/add_product.html', {"form": form})
class AddProductView(FormView):
    template_name = "hesabdari/add_product.html"
    form_class = AddProduct
    success_url = reverse_lazy("hesabdari:productlist")

    def form_valid(self, form):
        data = form.cleaned_data
        Product.objects.create(name=data["name"], price_product=data["price_product"], image=data["image"])
        return super().form_valid(form)


def delete_product_view(request, id):
    del_product = Product.objects.get(id=id)
    del_product.delete()
    return redirect("hesabdari:productlist")


class ProductListView(ListView):
    model = Product
    template_name = "hesabdari/product_list.html"
    context_object_name = "products"

# def list_product_view(request):
#     products = Product.objects.all()
#     return render(request, 'hesabdari/product_list.html', context={"products": products})
