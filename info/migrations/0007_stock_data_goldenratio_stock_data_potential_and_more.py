# Generated by Django 4.1.4 on 2023-12-15 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0006_alter_stock_data_earningsannouncement'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock_data',
            name='goldenratio',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='stock_data',
            name='potential',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='stock_data',
            name='cap',
            field=models.CharField(default=False, max_length=1),
        ),
    ]
