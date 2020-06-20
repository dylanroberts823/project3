# Generated by Django 3.0.6 on 2020-06-20 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0021_auto_20200607_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category_topping',
            name='category',
        ),
        migrations.AddField(
            model_name='category_topping',
            name='category',
            field=models.ManyToManyField(related_name='toppings', to='orders.Category'),
        ),
        migrations.RemoveField(
            model_name='item_topping',
            name='item',
        ),
        migrations.AddField(
            model_name='item_topping',
            name='item',
            field=models.ManyToManyField(related_name='toppings', to='orders.Item'),
        ),
    ]
