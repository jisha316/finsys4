# Generated by Django 4.0.4 on 2022-12-31 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0070_itemstock_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemstock',
            name='stocks',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
