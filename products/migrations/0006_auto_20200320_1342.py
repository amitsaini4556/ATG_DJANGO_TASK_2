# Generated by Django 2.2.10 on 2020-03-20 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200320_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='post_mode',
            field=models.CharField(default='0000', max_length=20),
        ),
    ]
