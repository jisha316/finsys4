# Generated by Django 4.0.4 on 2022-11-21 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_alter_purchasebill_item_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasebill_item',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='purchasedebit1',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
