from django.contrib import admin
from .models import Company, CompanyRequest


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "user",
        "address",
    )
    search_fields = (
        "name",
        "user",
    )
    

@admin.register(CompanyRequest)
class CompanyRequestAdmin(admin.ModelAdmin):
    list_display = (
        "company",
        "resume",
    )
    search_fields = (
        "company",
        "resume",
    )
