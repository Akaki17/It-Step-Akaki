# Generated by Django 5.1.3 on 2024-11-14 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_shope', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='category',
            table='categories',
        ),
        migrations.AlterModelTable(
            name='product',
            table='products',
        ),
    ]