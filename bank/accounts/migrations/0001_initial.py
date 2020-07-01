# Generated by Django 3.0.4 on 2020-07-01 21:56

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('surname', models.CharField(max_length=40)),
                ('place_of_resident', models.CharField(choices=[('alexeyevskaya', 'Alexeyevskaya'), ('kievskaya', 'Kievskaya'), ('paveletskaya', 'Paveletskaya'), ('kremlin', 'Kremlin'), ('polis', 'polis'), ('rizhskaya', 'Rizhskaya'), ('sevastopolskaya', 'Sevastopolskaya'), ('smolenskaya', 'Smolenskaya'), ('depot', 'Depot'), ('lubyanka', 'Lubyanka'), ('unknown', 'Unknown')], default='unknown', max_length=50)),
                ('profession', models.CharField(choices=[('soldier', 'Soldier'), ('stalker', 'Stalker'), ('bookman', 'Bookman'), ('internal_worker', 'Internal Worker'), ('other', 'Other'), ('unemployed', 'Unemployed'), ('commander', 'Commander'), ('shopkeeper', 'Shopkeeper')], default='unemployed', max_length=30)),
                ('status', models.CharField(choices=[('active', 'Active'), ('missing', 'Missing'), ('deceased', 'Deceased'), ('wanted', 'Wanted')], default='active', max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('changed_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'citizens_citizen',
            },
        ),
        migrations.CreateModel(
            name='CitizenAccount',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('account_balance', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.Citizen')),
            ],
        ),
        migrations.CreateModel(
            name='AccountHistory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.CitizenAccount')),
            ],
        ),
    ]
