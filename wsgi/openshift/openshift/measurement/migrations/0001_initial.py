# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2015, 4, 12, 15, 7, 26, 205000))),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('min_value', models.DecimalField(default=1.0, max_digits=6, decimal_places=2)),
                ('min_value_desc', models.CharField(default=b'Minimally', max_length=50)),
                ('max_value', models.DecimalField(default=4.0, max_digits=6, decimal_places=2)),
                ('max_value_desc', models.CharField(default=b'Maximally', max_length=50)),
                ('hidden', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2015, 4, 12, 15, 7, 26, 205000))),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('value', models.DecimalField(max_digits=6, decimal_places=2)),
                ('notes', models.CharField(max_length=200, null=True)),
                ('type', models.ForeignKey(to='measurement.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
        ),
        migrations.AddField(
            model_name='measurement',
            name='user',
            field=models.ForeignKey(to='measurement.User'),
            preserve_default=True,
        ),
    ]
