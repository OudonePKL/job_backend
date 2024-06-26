# Generated by Django 5.0.4 on 2024-05-08 07:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("resume", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Company name")),
                (
                    "address",
                    models.CharField(max_length=200, verbose_name="Company location"),
                ),
                ("phone", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "company_number",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="Company Registration Number",
                    ),
                ),
                (
                    "introduce",
                    models.TextField(blank=True, null=True, verbose_name="Introduce"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Business Owner",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CompanyRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="company.company",
                        verbose_name="Company",
                    ),
                ),
                (
                    "resume",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="resume.resume",
                        verbose_name="Resume",
                    ),
                ),
            ],
        ),
    ]
