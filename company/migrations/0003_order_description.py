# Generated by Django 5.0.4 on 2024-05-20 02:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("company", "0002_order_orderitem_delete_companyrequest"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
