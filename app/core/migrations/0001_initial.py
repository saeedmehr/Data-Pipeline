# Generated by Django 3.1.3 on 2022-01-02 23:10

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('wgs84_polygon', models.TextField()),
                ('the_geom', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='NonrelLocation',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('wgs84_polygon', models.TextField()),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='NonrelReservation',
            fields=[
                ('id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('customer_id', models.IntegerField()),
                ('start_latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('start_longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('srid', models.CharField(max_length=10)),
                ('net_price', models.IntegerField()),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('customer_id', models.IntegerField()),
                ('start_latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('start_longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('srid', models.CharField(max_length=10)),
                ('net_price', models.IntegerField()),
                ('the_geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]