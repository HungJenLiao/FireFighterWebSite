# Generated by Django 4.1.3 on 2022-12-05 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emergency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='案發日期')),
                ('unit', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=10)),
                ('detail', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]
