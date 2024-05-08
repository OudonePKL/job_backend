from django.db import models
from users.models import UserModel
from resume.models import Resume

class Company(models.Model):
    user = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, verbose_name="Business Owner"
    )
    name = models.CharField(max_length=100, verbose_name="Company name")
    address = models.CharField(max_length=200, verbose_name="Company location")
    phone = models.CharField(max_length=200, null=True, blank=True)
    company_number = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="Company Registration Number",
    )
    introduce = models.TextField(null=True, blank=True, verbose_name="Introduce")

    def __str__(self):
        return self.name

class CompanyRequest(models.Model):
    company = models.ForeignKey(Company, models.CASCADE, verbose_name="Company")
    resume = models.ForeignKey(Resume, models.PROTECT, verbose_name="Resume")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.company.name
    