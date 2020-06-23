# Generated by Django 3.0.6 on 2020-06-23 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0025_auto_20200622_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('CA', 'Carted'), ('PL', 'Placed'), ('PR', 'Preparing'), ('RE', 'Ready'), ('DE', 'Delivered'), ('CC', 'Cancelled by customer'), ('CR', 'Cancelled by restaurant')], default='CA', max_length=2),
        ),
    ]
