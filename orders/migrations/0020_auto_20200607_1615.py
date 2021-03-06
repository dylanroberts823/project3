# Generated by Django 3.0.6 on 2020-06-07 16:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0019_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('PL', 'Placed'), ('PR', 'Preparing'), ('RE', 'Ready'), ('DE', 'Delivered'), ('CC', 'Cancelled by customer'), ('CR', 'Cancelled by restaurant')], default='PL', max_length=2),
        ),
    ]
