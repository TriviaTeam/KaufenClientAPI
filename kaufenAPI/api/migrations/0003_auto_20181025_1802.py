# Generated by Django 2.1.1 on 2018-10-25 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20181025_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
