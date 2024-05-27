from django.contrib import admin
from .models import Company, Order, OrderItem, WebInfo


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "user",
        "address",
    )
    search_fields = (
        "name",
        "user",
    )
    
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(WebInfo)