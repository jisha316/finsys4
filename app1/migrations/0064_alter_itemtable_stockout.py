# Generated by Django 4.0.4 on 2022-12-10 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0063_itemtable_stockout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemtable',
            name='stockout',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
    ]
