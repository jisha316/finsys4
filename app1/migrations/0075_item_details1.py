# Generated by Django 4.0.4 on 2022-12-12 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0074_rename_item_item_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='details1',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
