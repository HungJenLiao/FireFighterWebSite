# Generated by Django 4.1.4 on 2023-02-14 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uploadFile', '0011_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emergency',
            name='car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='uploadFile.car'),
        ),
    ]
