# Generated by Django 3.2.12 on 2022-04-17 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='main_photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
