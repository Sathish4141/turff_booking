# Generated by Django 4.0.2 on 2023-06-24 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbooking',
            name='amount',
            field=models.BigIntegerField(default=0),
        ),
    ]
