# Generated by Django 3.0.6 on 2020-06-23 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0027_auto_20200623_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.FloatField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Item_Price',
        ),
    ]
