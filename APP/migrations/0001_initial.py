# Generated by Django 3.0.3 on 2021-02-25 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaSize',
            fields=[
                ('ps_id', models.AutoField(primary_key=True, serialize=False)),
                ('size', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PizzaTopping',
            fields=[
                ('pt_id', models.AutoField(primary_key=True, serialize=False)),
                ('topping', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('types', models.CharField(choices=[('Regular', 'Regular'), ('Square', 'Square')], max_length=100)),
                ('sizes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pizza_size', to='APP.PizzaSize')),
                ('toppings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pizza_topping', to='APP.PizzaTopping')),
            ],
        ),
    ]
