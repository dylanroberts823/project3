# Generated by Django 3.0.6 on 2020-06-07 16:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0020_auto_20200607_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order',
            field=models.CharField(default=django.utils.timezone.now, max_length=512),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
