# Generated by Django 3.2 on 2021-10-22 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mistershoppie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='normusers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('phone_number', models.TextField(max_length=10)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
