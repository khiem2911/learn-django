# Generated by Django 4.2.5 on 2023-09-25 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=264)),
                ('Last_Name', models.CharField(max_length=264)),
                ('Email', models.EmailField(max_length=264, unique=True)),
            ],
        ),
    ]
