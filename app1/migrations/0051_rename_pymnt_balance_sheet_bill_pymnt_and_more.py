# Generated by Django 4.0.4 on 2022-12-05 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0050_purchasedebit_cgst_purchasedebit_igst_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='balance_sheet',
            old_name='pymnt',
            new_name='bill_pymnt',
        ),
        migrations.AddField(
            model_name='balance_sheet',
            name='inv_pymnt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.payment'),
        ),
    ]
