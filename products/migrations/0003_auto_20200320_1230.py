# Generated by Django 2.2.10 on 2020-03-20 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='mode',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='body',
            field=models.TextField(default='000000'),
        ),
    ]
