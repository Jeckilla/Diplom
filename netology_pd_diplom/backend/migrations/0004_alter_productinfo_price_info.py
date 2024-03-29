# Generated by Django 5.0 on 2024-01-14 13:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_remove_product_price_productinfo_price_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinfo',
            name='price_info',
            field=models.FileField(upload_to='products/price/%Y/%m/%d', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['xls', 'xlsx'])]),
        ),
    ]
