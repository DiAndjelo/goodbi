# Generated by Django 3.1 on 2020-08-28 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200828_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='age',
            field=models.IntegerField(default=1, verbose_name='Age'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='passenger',
            name='pclass',
            field=models.IntegerField(default=0, verbose_name='Passenger class'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='passenger',
            name='sib_sp',
            field=models.IntegerField(default=0, verbose_name='SibSp'),
            preserve_default=False,
        ),
    ]