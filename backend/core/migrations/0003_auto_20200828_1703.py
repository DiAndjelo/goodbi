# Generated by Django 3.1 on 2020-08-28 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200828_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='age',
            field=models.IntegerField(verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='sib_sp',
            field=models.IntegerField(verbose_name='SibSp'),
        ),
    ]