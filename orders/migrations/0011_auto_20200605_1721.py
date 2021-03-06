# Generated by Django 3.0.6 on 2020-06-05 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20200605_1714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='extras',
        ),
        migrations.AddField(
            model_name='extras',
            name='category',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='orders.Categories'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='extras',
            name='item',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='orders.Items'),
            preserve_default=False,
        ),
    ]
