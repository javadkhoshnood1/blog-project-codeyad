from django.contrib import admin
from .models import Product, Customer


# Register your models here.
# admin.site.register(Product)
@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("__str__", "upload_image", "price_product", "percent_price")
    list_editable = ("price_product",)
    search_fields = ("name",)


# admin.site.register(Customer)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("__str__", "name", "phone_number")
    list_editable = ("name",)
    list_filter = ("all_costs", "product")
    search_fields = ("name",)
