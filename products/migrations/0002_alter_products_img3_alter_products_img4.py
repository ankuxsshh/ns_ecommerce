# Generated by Django 4.2 on 2024-01-14 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='img3',
            field=models.ImageField(blank=True, upload_to='Products/'),
        ),
        migrations.AlterField(
            model_name='products',
            name='img4',
            field=models.ImageField(blank=True, upload_to='Products/'),
        ),
    ]
