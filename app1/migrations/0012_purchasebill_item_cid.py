# Generated by Django 4.0.4 on 2022-11-21 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_alter_purchasebill_item_quantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasebill_item',
            name='cid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company'),
        ),
    ]
