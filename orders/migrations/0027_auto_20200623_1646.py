# Generated by Django 3.0.6 on 2020-06-23 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0026_auto_20200623_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='large_price',
        ),
        migrations.RemoveField(
            model_name='item',
            name='set_price',
        ),
        migrations.RemoveField(
            model_name='item',
            name='small_price',
        ),
        migrations.AddField(
            model_name='item_topping',
            name='price',
            field=models.FloatField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Item_Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(max_length=10)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Item')),
            ],
        ),
    ]
