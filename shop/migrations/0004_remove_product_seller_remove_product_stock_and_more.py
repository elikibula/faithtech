# Generated by Django 5.0 on 2025-06-19 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_seller_product_stock_product_stock_threshold_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='seller',
        ),
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
        migrations.RemoveField(
            model_name='product',
            name='stock_threshold',
        ),
    ]
