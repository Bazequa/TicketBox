# Generated by Django 4.1.5 on 2023-02-13 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketapp', '0014_alter_ticketapi_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pusers',
            name='role',
            field=models.CharField(choices=[('Manager', 'Manager'), ('Employee', 'Employee'), ('admin', 'admin')], max_length=100),
        ),
    ]
