# Generated by Django 5.0.4 on 2024-05-20 03:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("company", "0006_alter_orderitem_resume"),
        ("resume", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderitem",
            name="resume",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="resume.resume",
                verbose_name="Resume",
            ),
        ),
    ]