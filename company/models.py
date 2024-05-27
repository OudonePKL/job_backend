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


class Order(models.Model):
    STATUS_CHOICES = [
        ("READ", "Read"),
        ("UNREAD", "Unread"),
    ]

    company = models.ForeignKey(Company, models.CASCADE, verbose_name="Company")
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="UNREAD", verbose_name="Status"
    )

    def __str__(self):
        return f"ID: {self.id} - Company: {self.company.name} - Status: {self.status}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, models.CASCADE, null=True, blank=True, verbose_name="Resume")

    def __str__(self):
        return f"ID: {self.id} - Company: {self.order.company.name} - Resume: {self.resume.name}"


class WebInfo(models.Model):
    company_pdf = models.FileField(
        verbose_name="Company PDF", 
        blank=True, 
        null=True, 
        upload_to="webinfo/company",
    )
    employee_pdf = models.FileField(
        verbose_name="Employee PDF", 
        blank=True, 
        null=True, 
        upload_to="webinfo/employee",
    )
    
    def __str__(self):
        return f"ID: {self.id} - Company: {self.company_pdf} - Employee: {self.employee_pdf}"
    