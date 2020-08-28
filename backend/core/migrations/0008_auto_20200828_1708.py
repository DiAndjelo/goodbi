# Generated by Django 3.1 on 2020-08-28 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_passenger_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='age',
            field=models.IntegerField(default=0, verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='pclass',
            field=models.IntegerField(default=0, verbose_name='Passenger class'),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='sib_sp',
            field=models.IntegerField(default=0, verbose_name='SibSp'),
        ),
    ]