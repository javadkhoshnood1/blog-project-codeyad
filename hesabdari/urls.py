from django.urls import path
from . import views

app_name = 'hesabdari'

urlpatterns = [
    path('customerlist/', views.customer_list_view,name= "customerlist"),
    path('productlist/', views.list_product_view, name="productlist"),
    path('addcustomer/', views.add_customer_view ,name="addcustomer"),
    path('deltecustomer/<int:id>', views.delete_customer ,name="dalatecustomer"),
    path('addproduct/', views.add_product_view,name="addproduct"),
    path('deleteproduct/<int:id>', views.delete_product_view,name="deletproduct"),
    path('customer/<int:id>/', views.customer_taki_view ,name="coustomer_taki"),

]
