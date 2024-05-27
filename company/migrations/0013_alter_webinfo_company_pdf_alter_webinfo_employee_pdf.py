# Generated by Django 5.0.4 on 2024-05-27 03:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("company", "0012_alter_webinfo_company_pdf_alter_webinfo_employee_pdf"),
    ]

    operations = [
        migrations.AlterField(
            model_name="webinfo",
            name="company_pdf",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="webinfo/company",
                verbose_name="Company PDF",
            ),
        ),
        migrations.AlterField(
            model_name="webinfo",
            name="employee_pdf",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="webinfo/employee",
                verbose_name="Employee PDF",
            ),
        ),
    ]