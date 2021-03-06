# Generated by Django 3.0.6 on 2020-06-05 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20200605_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extras',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Categories'),
        ),
        migrations.AlterField(
            model_name='extras',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Items'),
        ),
        migrations.AlterField(
            model_name='items',
            name='large_price',
            field=models.FloatField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='set_price',
            field=models.FloatField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='small_price',
            field=models.FloatField(max_length=10, null=True),
        ),
    ]
