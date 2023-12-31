# Generated by Django 4.1.4 on 2023-12-15 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_portfolio_user_profile_remove_customuser_desc_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=20)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('Number', models.BigIntegerField(blank=True, null=True)),
                ('Portfolio_amount', models.BigIntegerField(blank=True, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('Desc', models.CharField(blank=True, max_length=2000, null=True)),
                ('occupation', models.CharField(blank=True, max_length=2000, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='User_Profile',
        ),
    ]
