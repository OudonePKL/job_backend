# Generated by Django 5.0.4 on 2024-05-20 03:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("company", "0005_alter_order_status"),
        ("resume", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderitem",
            name="resume",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="resume.resume",
                verbose_name="Resume",
            ),
        ),
    ]
