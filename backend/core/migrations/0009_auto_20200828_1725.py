# Generated by Django 3.1 on 2020-08-28 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200828_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='age',
            field=models.CharField(max_length=32, verbose_name='Age'),
        ),
    ]