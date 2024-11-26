# Generated by Django 4.2 on 2024-01-14 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('stock', models.BooleanField(default=True, null=True)),
                ('qty', models.CharField(max_length=5, null=True)),
                ('qcheck', models.CharField(max_length=5, null=True)),
                ('shortD', models.TextField(null=True)),
                ('discription', models.TextField(null=True)),
                ('img1', models.ImageField(upload_to='Products/')),
                ('img2', models.ImageField(upload_to='Products/')),
                ('img3', models.ImageField(upload_to='Products/')),
                ('img4', models.ImageField(upload_to='Products/')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
            ],
        ),
    ]
