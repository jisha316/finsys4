# Generated by Django 4.0.2 on 2022-12-08 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0058_remove_profit_loss_amount_remove_profit_loss_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='opening_balance_due',
        ),
    ]
