# Generated by Django 3.1 on 2020-08-28 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200828_1703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passenger',
            name='age',
        ),
        migrations.RemoveField(
            model_name='passenger',
            name='pclass',
        ),
        migrations.RemoveField(
            model_name='passenger',
            name='sib_sp',
        ),
    ]
