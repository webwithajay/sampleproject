# Generated by Django 4.2 on 2023-10-02 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_job'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='Firstname',
            new_name='Name',
        ),
        migrations.RemoveField(
            model_name='job',
            name='Lastname',
        ),
    ]