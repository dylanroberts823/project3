# Generated by Django 3.0.6 on 2020-06-22 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0024_auto_20200622_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='cat_topping',
            field=models.ManyToManyField(to='orders.Category_Topping'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='item_topping',
            field=models.ManyToManyField(to='orders.Item_Topping'),
        ),
    ]