# Generated by Django 3.1.5 on 2021-01-22 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ShippingAdress',
            new_name='ShippingAddress',
        ),
    ]
