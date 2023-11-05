# Generated by Django 4.2.3 on 2023-07-23 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDateTime', models.DateTimeField()),
                ('seats', models.IntegerField()),
                ('status', models.IntegerField(choices=[(1, 'Starting'), (2, 'SoldOut'), (3, 'Canceld'), (4, 'saling')])),
                ('eventModel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketing.eventmodel')),
                ('locationModel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketing.locationmodel')),
            ],
        ),
    ]