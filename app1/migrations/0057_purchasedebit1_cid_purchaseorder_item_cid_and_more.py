# Generated by Django 4.0.4 on 2022-12-06 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0056_creditperiod_cid_paymentmethod_cid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasedebit1',
            name='cid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company'),
        ),
        migrations.AddField(
            model_name='purchaseorder_item',
            name='cid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company'),
        ),
        migrations.AddField(
            model_name='purchasepayment1',
            name='cid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company'),
        ),
    ]
