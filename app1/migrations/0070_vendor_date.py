# Generated by Django 4.0.4 on 2022-12-12 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0069_vendor_opblnc_due'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
