# Generated by Django 4.2 on 2024-03-16 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_rename_name_customers_fname_customers_lname'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customers',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
