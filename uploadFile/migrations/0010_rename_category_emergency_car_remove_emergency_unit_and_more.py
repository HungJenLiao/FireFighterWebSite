# Generated by Django 4.1.4 on 2023-02-10 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadFile', '0009_delete_member'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emergency',
            old_name='category',
            new_name='car',
        ),
        migrations.RemoveField(
            model_name='emergency',
            name='unit',
        ),
        migrations.AddField(
            model_name='emergency',
            name='status',
            field=models.CharField(default=1, max_length=1),
            preserve_default=False,
        ),
    ]
