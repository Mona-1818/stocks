# Generated by Django 4.1.4 on 2023-12-16 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_userprofile_delete_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='Image',
        ),
    ]