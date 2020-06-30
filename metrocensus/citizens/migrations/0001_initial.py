# Generated by Django 3.0.4 on 2020-06-30 19:53

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
        ),
        migrations.CreateModel(
            name='CitizenFile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('desription', models.CharField(max_length=400)),
                ('result', models.CharField(max_length=200)),
                ('citizen_status_changed', models.BooleanField(default=False)),
                ('citizen', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='citizens.Citizen')),
            ],
        ),
    ]
