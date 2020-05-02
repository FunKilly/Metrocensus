# Generated by Django 3.0.4 on 2020-05-02 20:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CitizenFile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('desription', models.CharField(max_length=400)),
                ('result', models.CharField(max_length=200)),
                ('citizen_status_changed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ReasonOfDeath',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('surname', models.CharField(max_length=40)),
                ('profession', models.CharField(choices=[('soldier', 'Soldier'), ('stalker', 'Stalker'), ('bookman', 'Bookman'), ('internal_worker', 'Internal Worker'), ('other', 'Other'), ('unemployed', 'Unemployed'), ('commander', 'Commander'), ('shopkeeper', 'Shopkeeper')], default='other', max_length=30)),
                ('status', models.CharField(choices=[('active', 'Active'), ('missing', 'Missing'), ('deceased', 'Deceased'), ('wanted', 'Wanted')], default='active', max_length=30)),
                ('place_of_resident', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='citizens.Location')),
            ],
        ),
    ]
