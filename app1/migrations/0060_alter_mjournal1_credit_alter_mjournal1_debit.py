# Generated by Django 4.0.4 on 2022-12-09 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0059_remove_mjournal_account1_remove_mjournal_account2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mjournal1',
            name='credit',
            field=models.FloatField(default=''),
        ),
        migrations.AlterField(
            model_name='mjournal1',
            name='debit',
            field=models.FloatField(default=''),
        ),
    ]
