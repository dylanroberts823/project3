# Generated by Django 3.0.6 on 2020-06-05 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DinnerPlatters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platter', models.CharField(max_length=64)),
                ('price', models.FloatField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pastas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pasta', models.CharField(max_length=64)),
                ('price', models.FloatField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Salads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salad', models.CharField(max_length=64)),
                ('price', models.FloatField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SicPizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza', models.CharField(max_length=64)),
                ('small_price', models.FloatField(max_length=10)),
                ('large_price', models.FloatField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SubExtras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping', models.CharField(max_length=64)),
                ('price', models.FloatField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Subs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub', models.CharField(max_length=64)),
                ('small_price', models.FloatField(max_length=10)),
                ('large_price', models.FloatField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Toppings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping', models.CharField(max_length=64)),
            ],
        ),
    ]
