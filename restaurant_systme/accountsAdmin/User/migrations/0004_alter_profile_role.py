# Generated by Django 5.1.2 on 2024-11-24 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_profile_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('Cashier', 'Cashier'), ('Admin', 'Admin')], default='Cashier', max_length=10),
        ),
    ]