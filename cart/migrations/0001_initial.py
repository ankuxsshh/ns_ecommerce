# Generated by Django 4.2 on 2024-04-11 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('add_user', models.CharField(max_length=200, null=True)),
                ('item_title', models.CharField(max_length=250, null=True)),
                ('qty', models.IntegerField(null=True)),
                ('rate', models.IntegerField(null=True)),
                ('sub_total', models.IntegerField(default=1)),
            ],
        ),
    ]
