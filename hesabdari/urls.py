from django.urls import path
from . import views

app_name = 'hesabdari'

urlpatterns = [
    path('customerlist/', views.CustomerListView.as_view(), name="customerlist"),
    path('productlist/', views.ProductListView.as_view(), name="productlist"),
    path('addcustomer/', views.AddCustomerView.as_view(), name="addcustomer"),
    path('deltecustomer/<int:id>', views.delete_customer, name="dalatecustomer"),
    path('deleteproductcustomer/<int:idproduct>/<int:idcustomer>', views.deleteproductcustomer,
         name="dalateproductcustomer"),
    path('addproduct/', views.AddProductView.as_view(), name="addproduct"),
    path('deleteproduct/<int:id>', views.delete_product_view, name="deletproduct"),
    path('customer/<int:id>/', views.CustomerDetailView.as_view(), name="coustomer_taki"),

]
