# Generated by Django 3.0.4 on 2020-07-02 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='WealthStatus',
        ),
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AlterModelTable(
            name='payouthistory',
            table='payout_history',
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]