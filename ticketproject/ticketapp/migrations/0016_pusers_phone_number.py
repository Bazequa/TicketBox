# Generated by Django 4.1.5 on 2023-02-21 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketapp', '0015_alter_pusers_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='pusers',
            name='phone_number',
            field=models.IntegerField(default=0),
        ),
    ]