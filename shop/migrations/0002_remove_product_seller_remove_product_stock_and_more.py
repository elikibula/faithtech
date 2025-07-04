# Generated by Django 5.0 on 2025-06-19 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
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
        migrations.AlterField(
            model_name='product',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='Price in FJD', max_digits=10),
        ),
    ]
