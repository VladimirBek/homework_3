# Generated by Django 4.2.4 on 2023-09-10 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_product_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='published',
            field=models.BooleanField(default=False, verbose_name='статус публикации'),
        ),
    ]
