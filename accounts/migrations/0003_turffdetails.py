# Generated by Django 4.0.2 on 2023-04-29 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_turff_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turffdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turff_name', models.CharField(max_length=30)),
                ('turff_address', models.TextField()),
                ('turff_img', models.ImageField(blank=True, null=True, upload_to='')),
                ('contact', models.CharField(max_length=12)),
                ('court_fee', models.CharField(max_length=100)),
                ('court_size', models.CharField(max_length=50)),
                ('t_email', models.EmailField(max_length=50)),
                ('turff_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.turff_owner')),
            ],
        ),
    ]
