# Generated by Django 4.2.7 on 2023-11-13 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=150)),
                ('price', models.IntegerField(default=0)),
                ('description', models.TextField(max_length=150)),
                ('picture_url', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UpFile',
            fields=[
                ('upfile_id', models.AutoField(primary_key=True, serialize=False)),
                ('upfile_name', models.CharField(max_length=150)),
                ('upfile_url', models.CharField(max_length=150, null=True)),
            ],
        ),
    ]
