# Generated by Django 2.2 on 2021-05-23 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20210523_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='', upload_to='static/homepage/img/products'),
        ),
    ]
