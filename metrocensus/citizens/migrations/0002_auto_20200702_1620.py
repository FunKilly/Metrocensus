# Generated by Django 3.0.4 on 2020-07-02 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('citizens', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='citizen',
            table='citizen',
        ),
        migrations.AlterModelTable(
            name='citizenfile',
            table='citizen_file',
        ),
    ]